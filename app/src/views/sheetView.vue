<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen sheet">
    <form class="box"
          @submit.prevent="onSubmit">

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
          <div class="control">
            <input :id="getUniqueId(key)"
                   v-model="form[key]"
                   class="input"
                   type="text"
                   :placeholder="item"
            >
          </div>
        </template>

      </div>

      <div class="field mt-5">
        <button
            class="button is-success"
            :disabled="!hasChanges || !isValid"
        >
          {{ isLoading ? '...' : 'Update' }}
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
      isLoading: false,
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
      vm.isLoading = true
      return vm.$store.dispatch(`${SHEET.store}/get`, vm.itemId)
          .then(() => vm.resetForm())
          .catch(err => vm.handleError(err))
          .finally(() => vm.isLoading = false)
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
    /** Reset form */
    resetForm () {
      this.form = Object.assign({}, this.itemData)
    },
    /**
     * Submit Sheet details to API
     *
     * @returns {void|Promise<boolean>}
     */
    onSubmit () {
      if (this.isLoading) return
      if (!this.hasChanges) return
      if (!SHEET.isValid(this.form)) return

      this.isLoading = true

      const patchData = Object.keys(this.itemData).reduce((acc, current) => {
        if (this.itemData[current] === this.form[current]) return acc
        acc[current] = this.form[current]
        return acc
      }, {})

      const promise = this.$store.dispatch(
          `${SHEET.store}/patch`, { id: this.itemId, data: patchData })
          .then(() => this.$message.add({ message: 'Sheet updated.' }))
          .then(() => this.$router.push({ name: SHEET.views.list.name }))
          .catch(err => this.handleError(err))

      promise
          .finally(() => this.isLoading = false)

      return promise
    },
    /**
     * Add a new TimeSync via API
     *
     * @returns {void|Promise<boolean>}
     */
    onAddTimeSync () {
      const newTimeSync = TIMESYNC.init(this.itemId)

      return this.$store.dispatch(`${TIMESYNC.store}/post`,
          newTimeSync)
          .then((data) => {
            const sheetUpdate = Object.assign({}, this.itemData)
            sheetUpdate.time_sync_data.push(data)
            this.$store.commit(`${SHEET.store}/patch`, sheetUpdate)
          })
          .catch(err => this.handleError(err))
    }
  }
}
</script>
