import Vue from 'vue'
import { PROJECT } from '@/constants';
import HTTP from '@/services/HttpService'


/**
 * Creates a default Project Obj
 *
 * @return {Project} ProjectObj
 */
const defaultProjectObj = () => {
  return {
    id: -1,
    name: '',
    meta: '',
  }
}

/**
 * Returns initial store state
 *
 * @returns {object}
 */
function initState () {
  return {
    projects: []
  }
}

const getters = {
    /**
   * Gets a Project from state via ID
   *
   * @param {object}  state
   * @param {number}  id
   * @returns {Project|void}
   */
  getById: (state) => (id) => {
    return state.projects.find(item => item.id === id)
  }
}

const mutations = {
  /**
   * Sets the Project state
   *
   * @param {object}      state
   * @param {Project[]}   input
   */
  set: function (state, input) {
    Vue.set(state, 'projects', input)
  },
  /**
   * Add a Project
   *
   * @param {object}    state
   * @param {Project}   data    Project data
   */
  post: function (state, data) {
    state.projects.push(data)
  },
  /**
   * Patch a Project
   *
   * @param {object}    state
   * @param {Project}   data          Project data
   * @param {Boolean}   addIfMissing  Add to state if not found
   */
  patch: function (state, data, addIfMissing=true) {
    let updated = false
    state.projects.forEach(item => {
      if (item.id === data.id) {
        item = data
        updated = true
      }
    })

    if (!updated && !addIfMissing) return

    state.projects.push(data)
  },
  /**
   * Remove a Project
   *
   * @param {object}  state
   * @param {Number}  id
   */
  remove: function (state, id) {
    let count = state.projects.findIndex(item => item.id === id)
    if (count < 0) return
    state.projects.splice(count, 1)
  }
}
const actions = {
  /**
   * List Projects via API
   *
   * @param {object}  context
   * @param {object}  pageQuery
   * @return {Promise}
   */
  list: function (context, pageQuery) {
    return HTTP.get(PROJECT.API.GET, pageQuery)
    .then(({ data }) => {
      context.commit('set', data.data)
      return data.data
    })
  },
  /**
   * Get Project details via API
   *
   * @param {object}  context
   * @param {number}  id
   * @return {Promise}
   */
  get: function (context, id) {
    return HTTP.get(`${PROJECT.API.GET}/${id}/`)
    .then(({ data }) => {
      context.commit('patch', data.data)
      return data.data
    })
  },
  /**
   * Post Project details via API
   *
   * @param {object}  context
   * @param {Project}  data
   * @return {Promise}
   */
  post: function (context, data) {
    return HTTP.post(`${PROJECT.API.POST}/`, data)
    .then(({ data }) => {
      context.commit('post', data.data)
      return data.data
    })
  },
  /**
   * Patch Project details via API
   *
   * @param {object}    context
   * @param {Number}    id
   * @param {Project}   data
   * @return {Promise}
   */
  patch: function (context, {id, data}) {
    return HTTP.patch(`${PROJECT.API.PATCH}/${id}/`, data)
    .then(({ data }) => {
      context.commit('patch', data.data)
      return data.data
    })
  },
  /**
   * Delete Project via API
   *
   * @param {object}  context
   * @param {number}  id
   * @return {Promise}
   */
  remove: function (context, id) {
    return HTTP.remove(`${PROJECT.API.DELETE}/${id}/`)
    .then(({ data }) => {
      context.commit('remove', id)
      return data.data
    })
  }
}

export default {
  namespaced: true,
  state: initState(),
  getters: getters,
  mutations: mutations,
  actions: actions
}

