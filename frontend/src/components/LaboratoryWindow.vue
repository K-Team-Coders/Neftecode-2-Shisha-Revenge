<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-[98vh]">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="ml-72 w-full bg-frameBackground rounded-md border-[0.5px] duration-500"
    >
      <div class="p-4 h-full">
        <div>
          <div class="flex flex-col items-center justify-center w-full">
            <label
              for="dropzone-file"
              class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer duration-300 bg-neutral-100 dark:hover:bg-bray-800 dark:bg-gray-800 hover:bg-gray-100 dark:border-gray-700 dark:hover:border-gray-500 dark:hover:bg-gray-600"
              @dragover.prevent
              @drop="handleDrop"
            >
              <div class="flex flex-col items-center justify-center pt-5 pb-6">
                <svg
                  class="w-24 h-24 mb-1 text-gray-500 dark:text-gray-400"
                  aria-hidden="true"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 20 16"
                >
                  <path
                    stroke="currentColor"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
                  />
                </svg>
                <p class="mb-2 text-sm text-gray-500 dark:text-gray-400">
                  <span class="font-bold">Нажмите чтобы загрузить файл</span>
                  или
                  <span class="font-bold">перетащите его</span>
                </p>
                <p class="text-xs text-gray-500 dark:text-gray-400">.CSV</p>
              </div>
              <input
                id="dropzone-file"
                type="file"
                class="hidden"
                @change="handleFile"
              />
            </label>
            <p
              v-if="fileName"
              class="mt-2 text-md text-neutral-500 dark:text-gray-400"
            >
              {{ fileName }}
            </p>
          </div>
          <div class="flex pt-3 justify-end">
            <button
              @click.prevent="searchTender()"
              type="button"
              class="text-activeText px-5 py-2 rounded-md bg-blue-700 text-neutral-100 shadow-sm hover:bg-blue-900 duration-300"
            >
              Выполнить
            </button>
          </div>
        </div>
        <hr class="h-px my-8 bg-gray-400" />
        <div class="flex justify-end">
          <div class="shadow-md rounded-xl flex justify-end">
            <button
              :class="{
                'bg-blue-800 border-[1px] text-neutral-100':
                  isActiveButton === 1,
                'bg-transparent dark:text-neutral-100 border-[1px] text-neutral-800':
                  isActiveButton !== 1,
              }"
              @click="toggleButton(1)"
              class="px-4 py-2 rounded-l-xl duration-200"
            >
              Smiles
            </button>
            <button
              :class="{
                'bg-blue-800 border-[1px] text-neutral-100':
                  isActiveButton === 2,
                'bg-transparent border-[1px] dark:text-neutral-100 text-neutral-800':
                  isActiveButton !== 2,
              }"
              @click="toggleButton(2)"
              class="px-4 py-2 rounded-r-xl duration-200"
            >
              что то
            </button>
          </div>
        </div>
        <div class="">
          <div class="flex flex-col items-start w-full">
            <p class="text-activeText mb-1">что то 1</p>
            <input
              v-model="keyword1"
              @input="toggleSecondInput"
              class="rounded-md w-full h-12 pl-2.5 placeholder:text-sm shadow-sm"
              placeholder="Например: "
            />
          </div>
          <transition
            enter-active-class="duration-300"
            enter-from-class="opacity-0"
            enter-to-class="opacity-100"
            leave-active-class="duration-300"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
          >
            <div
              v-if="keyword1"
              class="flex flex-col items-start w-full pt-2 duration-300"
            >
              <p class="text-activeText mb-1">что то 2</p>
              <input
                v-model="keyword2"
                class="rounded-md w-full h-12 pl-2.5 placeholder:text-sm border-[1px] border-neutral-300 shadow-sm"
                placeholder="Например: "
              />
            </div>
          </transition>
          <div class="flex pt-4 justify-end">
            <button
              @click.prevent="searchTender()"
              type="button"
              class="text-activeText px-5 py-2 rounded-md bg-blue-700 text-neutral-100 shadow-sm hover:bg-blue-900 duration-300"
            >
              Выполнить
            </button>
          </div>
        </div>
        <hr class="h-px my-8 bg-gray-400" />
        <div class="">
          <div
            class="w-full items-center flex border-[1px] rounded-xl h-12 text-activeText"
          >
            <p class="text-lg px-3">confidence:</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import SidebarMain from "./SidebarMain.vue";

export default {
  components: {
    SidebarMain,
  },

  data() {
    return {
      keyword1: "",
      keyword2: "",
      date: null,
      isLoading: false,
      tenders_info: [],
      isError: false,
      isActiveButton: 1,
      fileName: null,
    };
  },

  methods: {
    toggleSecondInput() {
      if (this.keyword1) {
        this.keyword2 = "";
      }
    },
    handleFile(event) {
      const file = event.target.files[0];
      console.log("Загруженный файл:", file);
      this.fileName = file.name;
    },
    handleDrop(event) {
      event.preventDefault();
      const file = event.dataTransfer.files[0];
      console.log("Перетащенный файл:", file);
      this.fileName = file.name;
    },
    toggleButton(buttonIndex) {
      if (this.isActiveButton !== buttonIndex) {
        this.isActiveButton = buttonIndex;
      }
    },
    searchTender() {
      this.isLoading = true;
      let post_data = {
        element: this.keyword,
        date_1: this.timestampToDate_created,
        date_2: this.timestampToDate_finished,
      };
      console.log(post_data);
      axios
        .post(
          `http://${process.env.VUE_APP_SEARCH_TENDER_SERVICE_IP}/parse_tenderpro?element=${this.keyword}&date_1=${this.timestampToDate_created}&date_2=${this.timestampToDate_finished}'`
        )
        .then((response) => {
          console.log(response.data);
          this.tenders_info = response.data;
          this.isLoading = false;
        })
        .catch((error) => {
          this.isError = true;
        });
    },
    datetimeToDate(datetime) {
      const date = new Date(datetime);
      const day = date.getDate().toString().padStart(2, "0");
      const month = (date.getMonth() + 1).toString().padStart(2, "0");
      const year = date.getFullYear();
      const formattedDate = `${day}.${month}.${year}`;
      console.log(formattedDate);
      return formattedDate;
    },
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
    timestampToDate_created() {
      return this.datetimeToDate(this.date[0]);
    },
    timestampToDate_finished() {
      return this.datetimeToDate(this.date[1]);
    },
  },
};
</script>
<style>
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #535353;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #323232;
}
</style>
