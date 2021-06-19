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
            :disabled="!hasChanges"
        >
          {{ loading ? '...' : 'Update' }}
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
      loading: false,
      form: {}
    }
  },

  computed: {
    itemId () {
      return Number(this.$route.params.project)
    },
    itemData () {
      return this.$store.getters["project/getById"](this.itemId)
    },
    hasChanges () {
      if (!this.itemData) return false
      const source = Object.values(this.itemData).toString()
      const form = Object.values(this.form).toString()
      return source !== form
    }
  },

  created () {
    if (this.itemData) return
    this.loading = true
    return this.$store.dispatch('project/get', this.itemId)
    .then(data => {
      this.form = Object.assign({}, data)
    })
    .catch(err => this.handleError(err))
    .finally(() => this.loading = false)
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
      this.form = this.$options.data.call(this).form
    },
    /**
     * Submit Project details to API
     *
     * @returns {void|Promise<boolean>}
     */
    onSubmit () {
      if (this.loading) return
      if (!this.hasChanges) return
      if (!PROJECT.isValid(this.form)) return

      this.loading = true

      const patchData = Object.keys(this.itemData).reduce((acc, current) => {
        if (this.itemData[current] === this.form[current]) return acc
        acc[current] = this.form[current]
        return acc
      }, {})

      const promise = this.$store.dispatch(
          'project/patch', { id: this.itemId, data: patchData })
          .then(() => this.$message.add({ message: 'Project updated.' }))
          .then(() => this.$router.push({ name: 'project-list' }))
          .catch(err => this.handleError(err))

      promise
          .finally(() => this.loading = false)

      return promise
    }
  }
}
</script>
