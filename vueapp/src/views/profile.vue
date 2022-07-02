<template>
  <v-container  :class="{
        'container pa-4 my-12': $vuetify.breakpoint.smAndDown,
        'container pa-10 my-12': $vuetify.breakpoint.mdAndUp,
      }">
    <!-- avatar -->
    <v-row class="justify-center">
      <v-avatar size="80px">
        <img src="../assets/img/avatar.jpg" />
      </v-avatar>
    </v-row>
    <!-- name -->
    <v-row class="justify-center pb-5">
      <span class="title text-secondary py-2 font-weight-bold">{{ name }}</span>
    </v-row>
    <v-row>
        <v-col cols="12" lg="6">
          <p class="title text-secondary py-2 font-weight-bold">TITLE</p>
          <div class="row justify-space-between mb-5">
              <v-btn color="primary" @click="showModal = true">
                Select Exercise
              </v-btn>
              <v-btn
                class="mx-2"
                dark
                color="teal"
              >
                <v-icon dark>
                  mdi-format-list-bulleted-square
                </v-icon>
              </v-btn>
          </div>
          <v-img
            :aspect-ratio="16/9"
            
            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
          ></v-img>
          <v-btn
            class="ma-2"
            outlined
            color="indigo"
            @click="showSettingsModal = true"
          >
            Settings
          </v-btn>
        </v-col>
        <v-col cols="12" lg="6" class="v1">
          <span class="title text-secondary py-2 font-weight-bold">EXERCISE</span>
          <v-select
            :items="items"
            label="Up to Down"
            dense
            solo
            class="mt-5"
          ></v-select>
          <v-img
            :aspect-ratio="16/9"
            :height="200"
            src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
          ></v-img>
          <v-row class="mt-5 justify-center">
              <v-btn
                rounded
                color="primary"
                dark
              >
                Check Answer
              </v-btn>
              &nbsp;&nbsp;&nbsp;              
            <p class="py-2 font-weight-bold">Preview: </p>&nbsp;<p class="py-2 font-weight-bold">Correct</p>
          </v-row>
          <v-row class="mt-5 justify-space-between">
              <v-btn
                class="ma-2"
                outlined
                color="indigo"
                min-width="120"
              >
                Correct
              </v-btn>
              <v-btn
                class="ma-2"
                outlined
                color="indigo"
                min-width="120"
              >
                Easy
              </v-btn>
              <v-btn
                class="ma-2"
                outlined
                color="indigo"
                min-width="120"
              >
                Mistake
              </v-btn>
              <v-btn
                class="ma-2"
                outlined
                color="indigo"
                min-width="120"
              >
                Difficult
              </v-btn>
              <v-btn
                class="ma-2"
                outlined
                color="indigo"
                min-width="120"
              >
                Skip
              </v-btn>
          </v-row>
          <v-row class="mt-5 justify-space-between">
              <p>{{level[0]}}</p>
              <p>{{level[1]}}</p>
              <p>{{level[2]}}</p>
              <p>{{level[3]}}</p>
              <p></p>
          </v-row>
          <v-row class="mt-3 justify-space-between">
          <v-col cols="6" id="parent">
            <v-btn
              rounded
              color="primary"
              dark
              class="child"
            >
              Restart
            </v-btn>&nbsp;&nbsp;
            <v-select
              :items="items"
              :style="{width: '100px'}"
              label="In Order"
              dense
              outlined
              class="child"
            ></v-select>
          </v-col>
          <v-col cols="6">
            <v-btn
                rounded
                class="mt-3 float-end"
            >
              Close
            </v-btn>&nbsp;&nbsp;
            <v-btn
              rounded
              color="primary"
              dark
              class="mt-3 float-end"
            >
              Check Progress
            </v-btn>
            
          </v-col>
          </v-row>
        </v-col>
    </v-row>
    <transition name="fade" appear>
      <div class="modal-overlay"
          v-if="showModal"
          @click="showModal = false"></div>
    </transition>
    <transition name="pop" appear>
      <div class="modal"
            role="dialog"
            v-if="showModal"
            >
          <h1>Vue Transitions</h1>
          <v-list shaped dense min-height="240">
            <v-subheader>SUBJECTS</v-subheader>
            <v-list-item-group
              v-model="selectedItem"
              color="primary"
            >
              <v-list-item
                v-for="(item, i) in items"
                :key="i"
              >
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
           <v-file-input
            v-model="files"
            color="deep-purple accent-4"
            counter
            label="File input"
            multiple
            placeholder="Select your files"
            prepend-icon="mdi-paperclip"
            outlined
            :show-size="1000"
          >
            <template v-slot:selection="{ index, text }">
              <v-chip
                v-if="index < 2"
                color="deep-purple accent-4"
                dark
                label
                small
              >
                {{ text }}
              </v-chip>

              <span
                v-else-if="index === 2"
                class="text-overline grey--text text--darken-3 mx-2"
              >
                +{{ files.length - 2 }} File(s)
              </span>
            </template>
          </v-file-input>
          <v-btn color="primary" @click="onClickOk">OK</v-btn>&nbsp;&nbsp;&nbsp;
          <v-btn outlined color="indigo" @click="showModal = false">CANCEL</v-btn>
      </div>
    </transition>
<!--- Treeview Modal  --->
      <transition name="fade" appear>
        <div class="modal-overlay"
            v-if="showTreeviewModal"
            @click="showTreeviewModal = false"></div>
      </transition>
    <transition name="pop" appear>
      <div class="modal"
            role="dialog"
            v-if="showTreeviewModal"
            >
          <h1>Vue Transitions</h1>
          <v-treeview
            selectable
            :items="rows"
          ></v-treeview>
          <v-btn color="primary" @click="onTreeviewOk">OK</v-btn>
      </div>
    </transition>
<!-- Settings Modal -->
    <transition name="fade" appear>
      <div class="modal-overlay"
          v-if="showSettingsModal"
          @click="showSettingsModal = false"></div>
    </transition>
    <transition name="pop" appear>
      <div class="modal"
            role="dialog"
            v-if="showSettingsModal"
            >
          <h3>Waiting period for looking back</h3>
          <v-row>
              <v-col cols="6">Correct(not difficult)</v-col>
              <v-col cols="3"><vue-numeric-input v-model="not_difficult_value" :min="1" :max="30" size="110px" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="3">
                  <v-combobox
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <v-row>
              <v-col cols="6">Correct(easy)</v-col>
              <v-col cols="3"><vue-numeric-input v-model="easy_value" :min="1" :max="30" size="110px" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="3">
                  <v-combobox
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <v-row>
              <v-col cols="6">Wrong(mistake)</v-col>
              <v-col cols="3"><vue-numeric-input v-model="mistake_value" :min="1" :max="30" size="110px" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="3">
                  <v-combobox
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <v-row>
              <v-col cols="6">Wrong(difficult)</v-col>
              <v-col cols="3"><vue-numeric-input v-model="difficultvalue" :min="1" :max="30" size="110px" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="3">
                  <v-combobox
                    solo dense
                  ></v-combobox>
              </v-col>
          </v-row>
          <h3>Planning</h3>
          <v-row class="mb-4">
              <v-col cols="6">Number of exercises to do </v-col>
              <v-col cols="3"><vue-numeric-input v-model="number_exercises_value" :min="1" :max="30" size="110px" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
              <v-col cols="6">Day of exercise </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="mon"
                label="Mon"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="tue"
                label="Tue"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="wen"
                label="Wen"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="thu"
                label="Thu"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="fri"
                label="Fri"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="sat"
                label="Sat"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
              <v-col cols="2">
              <v-checkbox
                v-model="sun"
                label="Sun"
                color="primary"
                value="primary"
                hide-details
              ></v-checkbox>
              </v-col>
          </v-row>
          <h3>Reward</h3>
          <v-row class="mb-4">
              <v-col cols="6">points </v-col>
              <v-col cols="3"><vue-numeric-input v-model="points_value" :min="1" :max="30" size="110px" controls-type="updown" autofocus>
                              </vue-numeric-input>
              </v-col>
          </v-row>
          <v-btn color="primary" @click="onSettingsOk">OK</v-btn>&nbsp;&nbsp;&nbsp;
          <v-btn outlined color="indigo" @click="showSettingsModal = false">CANCEL</v-btn>
      </div>
    </transition>
  </v-container>
</template>

<script>
import VueNumericInput from 'vue-numeric-input'

export default {
  components: {
    VueNumericInput
  },
  data: () => ({
    not_difficult_value: 1,
    easy_value: 1,
    mistake_value: 1,
    difficult_value: 1,
    number_exercises_value: 1,
    points_value: 34,
    mon: false,
    tue: false,
    wed: false,
    thu: false,
    fri: false,
    sat: false,
    sun: false,
    rows: [
      {
        id: 1,
        name: 'Applications :',
        children: [
          { id: 2, name: 'Calendar : app' },
          { id: 3, name: 'Chrome : app' },
          { id: 4, name: 'Webstorm : app' },
        ],
      },
      {
        id: 5,
        name: 'Documents :',
        children: [
          {
            id: 6,
            name: 'vuetify :',
            children: [
              {
                id: 7,
                name: 'src :',
                children: [
                  { id: 8, name: 'index : ts' },
                  { id: 9, name: 'bootstrap : ts' },
                ],
              },
            ],
          },
          {
            id: 10,
            name: 'material2 :',
            children: [
              {
                id: 11,
                name: 'src :',
                children: [
                  { id: 12, name: 'v-btn : ts' },
                  { id: 13, name: 'v-card : ts' },
                  { id: 14, name: 'v-window : ts' },
                ],
              },
            ],
          },
        ],
      },
      {
        id: 15,
        name: 'Downloads :',
        children: [
          { id: 16, name: 'October : pdf' },
          { id: 17, name: 'November : pdf' },
          { id: 18, name: 'Tutorial : html' },
        ],
      },
      {
        id: 19,
        name: 'Videos :',
        children: [
          {
            id: 20,
            name: 'Tutorials :',
            children: [
              { id: 21, name: 'Basic layouts : mp4' },
              { id: 22, name: 'Advanced techniques : mp4' },
              { id: 23, name: 'All about app : dir' },
            ],
          },
          { id: 24, name: 'Intro : mov' },
          { id: 25, name: 'Conference introduction : avi' },
        ],
      },
    ],
    level: ["1days" ,"4weeks","4hours","1hours"],
    items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    showModal: false,
    showTreeviewModal: false,
    showSettingsModal: false,
    selectedItem: 1,
      items: [
        { text: 'History', icon: 'mdi-clock' },
        // { text: 'Audience', icon: 'mdi-account' },
        // { text: 'Conversions', icon: 'mdi-flag' },
      ],
      files: [],
  }),
  computed: {
    formData: {
      get: function () {
        return this.$store.getters["authPageModule/getFormData"];
      },
    },
    name() {
      if (!this.formData.firstName || !this.formData.lastName) return "Anas KASMI";
      else return this.formData.firstName + " " + this.formData.lastName;
    },
  },
  methods: {
    onClickOk() {
      this.showModal = false;
      this.showTreeviewModal = true;
    },
    onTreeviewOk() {
      this.showTreeviewModal = false;
    },
    backToPreviousPage() {
      this.$router.back();
    },
    updateInfo() {
      //fake post request
      this.axios
        .get("https://jsonplaceholder.typicode.com/todos/1")
        .then((response) => {
          this.$swal({
            title: "Updated",
            text: "Your profile was updated successfully",
            icon: "success",
            confirmButtonText: "Done",
          });
        })
        .catch((error) => {
          this.$swal({
            title: "Oops, Something went wrong ! ",
            text: error.message,
            icon: "warning",
          });
        });
    },
  },
};
</script>
<style scoped>
#parent { white-space: nowrap; }
.child { display: inline-block; }
</style>
