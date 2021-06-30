<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen sheet">
    <form class="box">

      <div v-for="(item, key) in itemData"
           :key="key"
           class="field"
      >
        <template v-if="key === 'time_sync_data'">
          <label
              class="label is-flex is-justify-content-space-between"
              :id="getUniqueId(key)"
          >
            Time Items
            <div class="tag is-link"
                 @click="onAddTimeSync">
              +Add
            </div>
          </label>
          <div class="control">
            <time-sync
                class="control"
                v-for="(time, idx) in item"
                :key="time.id || idx"
                :time-sync="time"
                update
                @update:time="onUpdateSheet"
            />
          </div>
        </template>
        <template v-else>
          <label
              class="label"
              :id="getUniqueId(key)"
          >
            {{ key }}
          </label>
          <div class="control"
               :class="{ 'is-loading': isLoading[key] }">
            <input :id="getUniqueId(key)"
                   :value="form[key]"
                   :placeholder="item"
                   class="input"
                   type="text"
                   @change="onUpdateSheet($event.target.value, key)"
            >
          </div>
        </template>

      </div>

      <div class="field mt-5">
        <button
            class="button is-success"
            :disabled="!hasChanges || !isValid"
        >
          Update
        </button>
      </div>

    </form>
  </div>

</template>

<script>
import { SHEET, TIMESYNC } from '@/constants'
import timeSync from '@/components/time-sync'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'sheet-view',

  mixins: [
    genericErrMixin
  ],

  components: {
    timeSync
  },

  data () {
    return {
      isLoading: {
        name: false,
        url: false,
        meta: false,
        data: false,
        ranking: false,
      },
      form: {}
    }
  },

  computed: {
    itemId () {
      return Number(this.$route.params.sheetId)
    },
    itemData () {
      return this.$store.getters[`${SHEET.store}/getById`](this.itemId)
    },
    isValid() {
      return SHEET.isValid(this.form)
    },
    hasChanges () {
      if (!this.itemData) return false

      let form = []
      let source = []
      Object.keys(this.itemData).forEach(item => {
        if (item !== 'time_sync_data') {
          source.push(this.itemData[item])
        }
      })
      Object.keys(this.form).forEach(item => {
        if (item !== 'time_sync_data') {
          form.push(this.form[item])
        }
      })

      return form.toString() !== source.toString()
    }
  },

  /** Returns Sheet data via API */
  beforeRouteEnter (to, from, next) {
    next(vm => {
      if (vm.itemData) {
        vm.resetForm()
        return
      }

      return vm.$store.dispatch(`${SHEET.store}/get`, vm.itemId)
          .then(() => vm.onResetForm())
          .catch(err => vm.handleError(err))
    })
  },

  methods: {
    /**
     * Simple string id generator
     *
     * @params {string}   input
     * @returns {string}
     */
    getUniqueId (input) {
      return 'id-' + input
    },
    /** Reset form data */
    onResetForm () {
      this.form = Object.assign({}, this.itemData)
    },
    /**
     * Update a Sheet with patch data
     *
     * @param {string|number|date}  input
     * @param {string}              type
     * @returns {Promise<boolean>|void}
     */
    onUpdateSheet (input, type) {
      if (this.isLoading[type]) return
      this.isLoading[type] = true

      return this.$store.dispatch(`${SHEET.store}/patch`, {
        id: this.itemId, data: { id: this.itemId, [type]: input }
      })
          .then((data) => this.form = data)
          .then(() => this.$message.add({
            message: 'Sheet updated.', timeDisplay: 3
          }))
          .catch(err => this.handleError(err))
          .finally(() => this.isLoading[type] = false)
    },
    /**
     * Get latest version of Sheet via API
     *
     * @returns {void|Promise<boolean>}
     */
    onUpdate() {
      if (this.isLoading) return
      this.isLoading = true
      return this.$store.dispatch(`${SHEET.store}/get`,
          this.itemId)
          .then((data) => this.form = data)
          .catch(err => this.handleError(err))
          .finally(() => this.isLoading = false)
    },
    /**
     * Add a new TimeSync via API
     *
     * @returns {void|Promise<boolean>}
     */
    onAddTimeSync() {
      if (this.isLoading) return

      const newTimeSync = TIMESYNC.init(this.itemId)
      return this.$store.dispatch(`${TIMESYNC.store}/post`, newTimeSync)
          .then(() => this.onUpdate())
          .catch(err => this.handleError(err))
    }
  }
}
</script>
