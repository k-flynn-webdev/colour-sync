<template>
  <div class="column is-7-tablet1 is-6-desktop1 is-4-widescreen1 project">
    <div class="table-container">
      <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
        <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Owner</th>
          <th>Meta</th>
          <th>Updated</th>
          <th>Created</th>
          <th>Deleted</th>
        </tr>
        </thead>
        <tbody>
        <tr
            v-for="(item, key) in projects"
            :key="key"
        >
          <td>{{ item.id }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.owner || '--' }}</td>
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
import { PROJECT } from '@/constants'
import { genericErrMixin } from '@/plugins/genericErrPlugin'

export default {
  name: 'project-list',

  mixins: [
    genericErrMixin
  ],

  data () {
    return {
      loading: false,
    }
  },

  computed: {
    projects () {
      return this.$store.state.project.projects
    }
  },

  created () {
    return this.getProjectsList()
  },

  methods: {
    /** Returns projects list via API
     *
     * @returns {Promise|void}
     */
    getProjectsList () {
      if (this.loading) return
      this.loading = true
      const pageQuery = this.$route.query.page || 0
      const promise = this.$store.dispatch("project/list", pageQuery)
          .catch(err => this.handleError(err))

      promise.finally(() => this.loading = false)
      return promise
    }
  }
}
</script>
