<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen project">
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
          {{ isLoading ? '...' : 'Update' }}
        </button>
      </div>

    </form>
  </div>

</template>

<script>
import { PROJECT } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'project-view',

  mixins: [
    genericErrMixin
  ],

  data () {
    return {
      isLoading: false,
      form: {}
    }
  },

  computed: {
    itemId () {
      return Number(this.$route.params.projectId)
    },
    itemData () {
      return this.$store.getters[`${PROJECT.store}/getById`](this.itemId)
    },
    isValid() {
      return PROJECT.isValid(this.form)
    },
    hasChanges () {
      if (!this.itemData) return false
      const source = Object.values(this.itemData).toString()
      const form = Object.values(this.form).toString()
      return source !== form
    }
  },

  /** Returns Project data via API */
  beforeRouteEnter (to, from, next) {
    next(vm => {
      if (vm.itemData) {
        vm.resetForm()
        return
      }
      vm.isLoading = true
      return vm.$store.dispatch(`${PROJECT.store}/get`, vm.itemId)
          .then(() => vm.resetForm())
          .catch(err => vm.handleError(err))
          .finally(() => vm.isLoading = false)
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
     * Submit Project details to API
     *
     * @returns {void|Promise<boolean>}
     */
    onSubmit () {
      if (this.isLoading) return
      if (!this.hasChanges) return
      if (!PROJECT.isValid(this.form)) return

      this.isLoading = true

      const patchData = Object.keys(this.itemData).reduce((acc, current) => {
        if (this.itemData[current] === this.form[current]) return acc
        acc[current] = this.form[current]
        return acc
      }, {})

      const promise = this.$store.dispatch(
          `${PROJECT.store}/patch`, { id: this.itemId, data: patchData })
          .then(() => this.$message.add({ message: 'Project updated.' }))
          .then(() => this.$router.push({ name: PROJECT.views.list.name }))
          .catch(err => this.handleError(err))

      promise
          .finally(() => this.isLoading = false)

      return promise
    }
  }
}
</script>
