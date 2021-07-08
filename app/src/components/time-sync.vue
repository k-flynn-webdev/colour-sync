<template>
  <div class="time-sync">

    <div v-if="short" class="short span-comma">
      <span class="id">[{{ timeSync.id }}]</span>
      <span class="meta">{{ timeSync.meta }}</span>
      <span class="date">{{ timeSync.date | itemDate }}</span>
      <span class="duration-type">{{ timeSync.durationType }}</span>
      <span class="duration-val">{{ timeSync.durationVal }}</span>
    </div>

    <form v-if="update"
          class="mb-4 p-1 has-border-background has-border-radius">
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">ID {{ timeSync.id }}</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control"
               :class="{ 'is-loading': isLoading.meta }">
              <input
                  :value="meta"
                  class="input"
                  type="text"
                  placeholder="Meta"
                  @change="patchTimeSync($event.target.value, 'meta')"
              >
            </p>
          </div>
        </div>
      </div>
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Date</label>
        </div>
        <div class="field-body">
          <div class="field">
            <p class="control is-expanded"
               :class="{ 'is-loading': isLoading.date }">
              <input
                  v-model="date"
                  class="input"
                  type="date"
                  placeholder="Choose a date">
            </p>
          </div>
        </div>
      </div>
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">Duration</label>
        </div>
        <div class="field-body">

          <div class="field has-addons">
            <div class="control"
                 :class="{ 'is-loading': isLoading.duration }">
              <div class="select">
                <select v-model="durationType">
                  <option
                      v-for="(option, key) in optionsDuration"
                      :key="key"
                      :value="key">
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>
            <p class="control is-expanded"
               :class="{ 'is-loading': isLoading.duration }">
              <input
                  v-model="durationVal"
                  class="input"
                  type="number"
                  step="1"
                  min="1"
                  max="365"
                  placeholder="7">
            </p>
          </div>

        </div>
      </div>
      <div v-if="remove"
           class="tag is-link has-background-danger has-fill-white"
           @click="onDeleteTimeSync">
        <cross-icon />
      </div>
    </form>

  </div>
</template>

<script>
import { TIMESYNC, REPEAT_CHOICES, DURATION_CHOICES } from '@/constants'
import crossIcon from '@/assets/cross'
import { genericErrMixin } from '@/plugins/genericErrPlugin'


export default {
  name: 'time-sync',

  components: { crossIcon },

  mixins: [
    genericErrMixin
  ],

  props: {
    /** @type {Boolean} Show a short non-interactive object */
    short: {
      required: false,
      default: false,
      type: Boolean
    },
    /** @type {Boolean} Allow TimeSync to be updated */
    update: {
      required: false,
      default: false,
      type: Boolean
    },
    /** @type {Boolean} Allow TimeSync to be removed */
    remove: {
      required: false,
      default: false,
      type: Boolean
    },
    /** @type {TimeSync} */
    timeSync: {
      required: true,
      type: Object
    }
  },

  data () {
    return {
      isLoading: {
        meta: false,
        date: false,
        durationType: false,
        durationVal: false,
      }
    }
  },

  computed: {
    optionsRepeat () { return REPEAT_CHOICES },
    optionsDuration () { return DURATION_CHOICES },
    meta: {
      get () { return this.timeSync.meta },
    },
    date: {
      get () { return this.timeSync.date },
      set (input) { return this.patchTimeSync(input, 'date') }
    },
    durationType: {
      get () { return this.timeSync.durationType },
      set (input) { return this.patchTimeSync(input, 'durationType') }
    },
    durationVal: {
      get () { return this.timeSync.durationVal },
      set (input) { return this.patchTimeSync(input, 'durationVal') }
    },
  },

  methods: {
    /**
     * Update a TimeSync with patch data
     *
     * @param {string|number|date}  input
     * @param {string}              type
     * @returns {Promise<boolean>|void}
     */
    patchTimeSync (input, type) {
      if (this.isLoading[type]) return
      this.isLoading[type] = true

      return this.$store.dispatch(`${TIMESYNC.store}/patch`, {
        id: this.timeSync.id, data: { id: this.timeSync.id, [type]: input }
      })
          .then(() => this.$emit('update:time'))
          .catch(err => this.handleError(err))
          .finally(() => this.isLoading[type] = false)
    },
    /**
     * Delete TimeSync via API
     *
     * @returns {void|Promise<boolean>}
     */
    onDeleteTimeSync() {
      return this.$store.dispatch(`${TIMESYNC.store}/remove`,
          this.timeSync.id)
          .then(() => this.$emit('update:time'))
          .catch(err => this.handleError(err))
    },
  }
}
</script>
