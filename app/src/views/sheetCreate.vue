<template>
  <div class="column is-7-tablet is-6-desktop is-4-widescreen sheet">
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
                 maxlength="99"
                 placeholder="e.g. new sheet 2021"
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
                 minlength="5"
                 maxlength="999"
                 placeholder="eg your notes: release by xxx date?"
          >
        </div>
      </div>
      <div class="field">
        <label for="id-url"
               class="label">
          URL
        </label>
        <div class="control">
          <input id="id-url"
                 v-model="form.url"
                 type="text"
                 class="input"
                 minlength="5"
                 maxlength="99"
                 placeholder="eg release-2020"
          >
        </div>
      </div>
      <div class="field">
        <label for="id-data"
               class="label">
          Data
        </label>
        <div class="control">
          <input id="id-data"
                 v-model="form.data"
                 type="text"
                 class="input"
                 required
                 minlength="5"
                 maxlength="99999"
                 placeholder="eg all your css styles to be applied"
          >
        </div>
      </div>
      <div class="field">
        <label for="id-ranking"
               class="label">
          Ranking
        </label>
        <div class="control">
          <input id="id-ranking"
                 v-model="form.ranking"
                 type="number"
                 class="input"
                 min="1"
                 max="999"
                 required
                 placeholder="eg 1 - 999, bigger will always override a smaller sheet"
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
import { SHEET } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'sheet-create',

  mixins: [
    genericErrMixin
  ],

  data () {
    return {
      isLoading: false,
      form: SHEET.init(this.projectId)
    }
  },

  computed: {
    isValid () {
      return SHEET.isValid(this.form)
    },
    projectId () { return Number(this.$route.params.projectId) || -1 }
  },

  mounted () {
    this.onReset()
  },

  methods: {
    /** Reset form */
    onReset () {
      this.form = this.$options.data.call(this).form
      this.form.project = this.projectId
    },
    /**
     * Submit Sheet details to API
     *
     * @returns {Promise|void}
     */
    onSubmit () {
      if (this.isLoading) return
      if (!this.isValid) return

      this.isLoading = true

      const promise = this.$store.dispatch('sheet/post', this.form)
          .then(() => this.$message.add({ message: 'Sheet created.' }))
          .then(() => this.$router.push({ name: 'sheet-list' }))
          .catch(err => this.handleError(err))

      promise
          .finally(() => this.isLoading = false)

      return promise
    }
  }
}
</script>
