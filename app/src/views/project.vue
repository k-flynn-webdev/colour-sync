<template>
  <div class="column is-5-tablet is-4-desktop is-3-widescreen project">
    <form class="box"
          @submit.prevent="submit">
      <div class="field">
        <label for="id-name" class="label">
          Name
        </label>
        <div class="control">
          <input id="id-name"
                 v-model="form.name"
                 class="input"
                 type="string"
                 minlength="6"
                 placeholder="e.g. new project 2021"
                 required
          >
        </div>
      </div>
      <div class="field">
        <label for="id-meta"
               class="label">
          Meta
        </label>
        <div class="control">
          <input id="id-meta"
                 v-model="form.meta"
                 type="string"
                 placeholder="eg your notes: release by xxx date?"
                 class="input"
          >
        </div>
      </div>

      <div class="field mt-5">
        <button class="button is-success">
          {{ loading ? '...' : 'Login' }}
        </button>
      </div>

    </form>
  </div>

</template>

<script>
import { PROJECT } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'project',

  mixins: [
    genericErrMixin
  ],

  data () {
    return {
      loading: false,
      form: {
        name: '',
        meta: '',
      }
    }
  },

  methods: {
    /** Reset Register details */
    resetForm () {
      this.form = this.$options.data.form.call(this)
    },
    /**
     * Submit Login details to API for authentication
     *
     * @returns {void|Promise<boolean>}
     */
    submit () {
      if (this.loading) return
      if (!PROJECT.isValid(this.form)) return

      this.loading = true

      return this.$store.dispatch('api/getCSRF')
      .then(() => this.$store.dispatch('project/post', this.form))
      .then(() => {
        this.resetForm()
        this.$router.push({ name: PROJECT.route.name })
      })
      .catch(err => this.handleError(err))
      .finally(() => this.loading = false)
    }
  }
}
</script>
