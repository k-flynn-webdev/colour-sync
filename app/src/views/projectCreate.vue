<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen project">
    <form class="box"
          @reset="onReset"
          @submit.prevent="onSubmit">
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
        <label for="id-url" class="label">
          URL
        </label>
        <div class="control">
          <input id="id-url"
                 v-model="form.url"
                 class="input"
                 type="text"
                 minlength="4"
                 placeholder="e.g. fancy-url"
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
        <button
            class="button is-success"
            :disabled="!isValid"
        >
          {{ isLoading ? '...' : 'Create' }}
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
      isLoading: false,
      form: PROJECT.init()
    }
  },

  computed: {
    isValid() {
      return PROJECT.isValid(this.form)
    }
  },

  methods: {
    /** Reset form */
    onReset () {
      this.form = this.$options.data.call(this).form
    },
    /**
     * Submit Project details to API
     *
     * @returns {Promise|void}
     */
    onSubmit () {
      if (this.isLoading) return
      if (!this.isValid) return

      this.isLoading = true

      const promise = this.$store.dispatch(`${PROJECT.store}/post`, this.form)
          .then(() => this.$message.add({ message: 'Project created.' }))
          .then(() => this.$router.push({ name: PROJECT.views.list }))
          .catch(err => this.handleError(err))

      promise
          .finally(() => this.isLoading = false)

      return promise
    }
  }
}
</script>
