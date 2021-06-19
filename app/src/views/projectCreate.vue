<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen project">
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
                 type="text"
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
                 type="text"
                 class="input"
                 placeholder="eg your notes: release by xxx date?"
          >
        </div>
      </div>

      <div class="field mt-5">
        <button class="button is-success">
          {{ loading ? '...' : 'Create' }}
        </button>
      </div>

    </form>
  </div>

</template>

<script>
import { PROJECT } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'project-create',

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
    /** Reset form */
    resetForm () {
      this.form = this.$options.data.call(this).form
    },
    /**
     * Submit Project details to API
     *
     * @returns {void|Promise<boolean>}
     */
    submit () {
      if (this.loading) return
      if (!PROJECT.isValid(this.form)) return

      this.loading = true

      return this.$store.dispatch('project/post', this.form)
          .then(({ data }) => {
            this.$message.add({ message: 'Project created.' })
            this.$router.push({ name: 'project-view', params: { project: data.id } })
          })
          .catch(err => this.handleError(err))
          .finally(() => this.loading = false)
    }
  }
}
</script>
