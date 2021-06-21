<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen sheet">
    <form class="box"
          @submit.prevent="onSubmit">

      <div v-for="(item, key) in itemData"
           :key="key"
           class="field"
      >
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
      </div>

      <div class="field mt-5">
        <button
            class="button is-success"
            :disabled="!hasChanges || !isValid"
        >
          {{ loading ? '...' : 'Update' }}
        </button>
      </div>

    </form>
  </div>

</template>

<script>
import { SHEET } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'sheet-view',

  mixins: [
    genericErrMixin
  ],

  data () {
    return {
      loading: false,
      form: {}
    }
  },

  computed: {
    itemId () {
      return Number(this.$route.params.sheet)
    },
    itemData () {
      return this.$store.getters["sheet/getById"](this.itemId)
    },
    isValid() {
      return SHEET.isValid(this.form)
    },
    hasChanges () {
      if (!this.itemData) return false
      const source = Object.values(this.itemData).toString()
      const form = Object.values(this.form).toString()
      return source !== form
    }
  },

  /** Returns Sheet data via API */
  beforeRouteEnter (to, from, next) {
    next(vm => {
      if (vm.itemData) {
        vm.resetForm()
        return
      }
      vm.loading = true
      return vm.$store.dispatch('sheet/get', vm.itemId)
          .then(() => vm.resetForm())
          .catch(err => vm.handleError(err))
          .finally(() => vm.loading = false)
    })
  },

  methods: {
    /**
     *  Simple string id generator
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
      if (this.loading) return
      if (!this.hasChanges) return
      if (!SHEET.isValid(this.form)) return

      this.loading = true

      const patchData = Object.keys(this.itemData).reduce((acc, current) => {
        if (this.itemData[current] === this.form[current]) return acc
        acc[current] = this.form[current]
        return acc
      }, {})

      const promise = this.$store.dispatch(
          'sheet/patch', { id: this.itemId, data: patchData })
          .then(() => this.$message.add({ message: 'Sheet updated.' }))
          .then(() => this.$router.push({ name: 'sheet-list' }))
          .catch(err => this.handleError(err))

      promise
          .finally(() => this.loading = false)

      return promise
    }
  }
}
</script>
