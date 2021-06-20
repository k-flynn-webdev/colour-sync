<template>
  <div class="column is-7-tablet1 is-6-desktop1 is-4-widescreen1 project">
    <div class="table-container">
      <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
        <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>URL</th>
          <th>Owner</th>
          <th>Project</th>
          <th>Data</th>
          <th>Ranking</th>
          <th>Meta</th>
          <th>Updated</th>
          <th>Created</th>
          <th>Deleted</th>
        </tr>
        </thead>
        <tbody>
        <tr
            v-for="(item, key) in sheets"
            :key="key"
        >
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.url }}</td>
          <td>{{ item.owner || '--' }}</td>
          <td>{{ item.project }}</td>
          <td>{{ item.data }}</td>
          <td>{{ item.ranking }}</td>
          <td>{{ item.meta }}</td>
          <td>{{ item.updatedAt | itemDate | itemIsNull }}</td>
          <td>{{ item.createdAt | itemDate | itemIsNull }}</td>
          <td>{{ item.deletedAt | itemDate | itemIsNull }}</td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>

</template>

<script>
import { SHEET } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'sheet-list',

  mixins: [
    genericErrMixin
  ],

  data () {
    return {
      loading: false,
    }
  },

  computed: {
    sheets () {
      return this.$store.state.sheet.sheets
    }
  },

  created () {
    return this.getSheetList()
  },

  methods: {
    /** Returns Sheets list via API
     *
     * @returns {Promise|void}
     */
    getSheetList () {
      if (this.loading) return
      this.loading = true
      const pageQuery = this.$route.query.page || 0
      const promise = this.$store.dispatch("sheet/list", pageQuery)
          .catch(err => this.handleError(err))

      promise.finally(() => this.loading = false)
      return promise
    }
  }
}
</script>
