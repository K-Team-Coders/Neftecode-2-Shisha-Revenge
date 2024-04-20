import torch
from transformers import AutoModel, AutoTokenizer
import pandas as pd
from loguru import logger

class MolEmbeddingsExtractor:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
        
    def tokenize_smiles(self, smiles):
        tokens = self.tokenizer.encode(smiles, add_special_tokens=True)
        input_ids = torch.tensor(tokens).unsqueeze(0)  # добавляем размерность пакета
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
        return input_ids, attention_mask
    
    def get_smiles_embeddings(self, smiles_list):
        mol_embeddings_list = []
        
        for smiles in smiles_list:
            input_ids, attention_mask = self.tokenize_smiles(smiles)
            with torch.no_grad():
                outputs = self.model(input_ids, attention_mask=attention_mask)
            mol_embeddings = outputs[0].mean(dim=1)
            mol_embeddings_list.append(mol_embeddings)
        
        mol_embeddings = torch.cat(mol_embeddings_list).mean(dim=0)
        return mol_embeddings.numpy()
    
    def process_dataframe(self, input_df):
        frame = pd.DataFrame(columns=['blend_id','smiles','oil_property_param_value','mixed_smiles'])
        blend_ids = input_df['blend_id'].unique()
        
        
        for blend_id in blend_ids:
            pivot_table = input_df[input_df['blend_id'] == blend_id]
            smiles_list = pivot_table['smiles'].values.tolist()
            smiles_embs = self.get_smiles_embeddings(smiles_list)
            pivot_table["mixed_smiles"] = [smiles_embs] * len(pivot_table)  # Repeat the numpy array to match the DataFrame length
            frame = pd.concat([frame, pivot_table], axis=0, ignore_index=True)
        
        return frame

if __name__ == "__main__":
    model_name = "seyonec/ChemBERTa-zinc-base-v1"
    extractor = MolEmbeddingsExtractor(model_name)
    
    df_smiles_train = pd.read_csv(r"..\data\smiles_train_set.csv")
    df_smiles_test=pd.read_csv(r"..\data\smiles_test_set_public.csv")
    train_set = extractor.process_dataframe(df_smiles_train)
    test_set = extractor.process_dataframe(df_smiles_test)
    