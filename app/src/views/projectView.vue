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
        <div class="control"
             :class="{ 'is-loading': isLoading[key] }">
          <input :id="getUniqueId(key)"
                 :value="form[key]"
                 :placeholder="item"
                 class="input"
                 type="text"
                 @change="onUpdateProject($event.target.value, key)"
          >
        </div>
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
      isLoading: {
        name: false,
        meta: false,
      },
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
        vm.onResetForm()
        return
      }

      return vm.$store.dispatch(`${PROJECT.store}/get`, vm.itemId)
          .then(() => vm.onResetForm())
          .catch(err => vm.handleError(err))
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
    onResetForm () {
      this.form = Object.assign({}, this.itemData)
    },
    /**
     * Update a Project with patch data
     *
     * @param {string|number|date}  input
     * @param {string}              type
     * @returns {Promise<boolean>|void}
     */
    onUpdateProject (input, type) {
      if (this.isLoading[type]) return
      this.isLoading[type] = true

      return this.$store.dispatch(`${PROJECT.store}/patch`, {
        id: this.itemId, data: { id: this.itemId, [type]: input }
      })
          .then((data) => this.form = data)
          .then(() => this.$message.add({
            message: 'Project updated.', timeDisplay: 3
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
      return this.$store.dispatch(`${PROJECT.store}/get`,
          this.itemId)
          .then((data) => this.form = data)
          .catch(err => this.handleError(err))
    },
  }
}
</script>
