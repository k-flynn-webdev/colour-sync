<template>
  <div class="column is-7-tablet1 is-6-desktop1 is-4-widescreen1 project">
    <div class="table-container">
      <progress v-if="isLoading" class="progress is-large is-info" max="100">60%</progress>
      <table v-else class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
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
            @click="onItemSelect(item.id)"
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
      isLoading: false,
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
      if (this.isLoading) return
      this.isLoading = true
      const pageQuery = this.$route.query.page || 0
      const promise = this.$store.dispatch("sheet/list", pageQuery)
          .catch(err => this.handleError(err))

      promise.finally(() => this.isLoading = false)
      return promise
    },
    /**
     * View Sheet via ID
     *
     * @param {number} id   item id
     * @returns {promise}
     */
    onItemSelect(id) {
      return this.$router.push({
        name: 'sheet-view',
        params: { sheet: id }
      })
    }
  }
}
</script>
