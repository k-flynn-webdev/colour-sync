import Vue from 'vue'
import { TIMESYNC } from '@/constants';
import HTTP from '@/services/HttpService'


/**
 * Returns initial store state
 *
 * @returns {object}
 */
function initState () {
  return {
    timesync: []
  }
}

const getters = {
  /**
   * Gets a TimeSync from state via ID
   *
   * @param {object}  state
   * @param {number}  id
   * @returns {TimeSync|void}
   */
  getById: (state) => (id) => {
    return state.timesync.find(item => item.id === id)
  }
}

const mutations = {
  /**
   * Sets the TimeSync state
   *
   * @param {object}      state
   * @param {TimeSync[]}  input
   */
  set: function (state, input) {
    Vue.set(state, 'timesync', input)
  },
  /**
   * Add a TimeSync
   *
   * @param {object}    state
   * @param {TimeSync}  data    timesync data
   */
  post: function (state, data) {
    state.timesync.push(data)
  },
  /**
   * Patch a TimeSync
   *
   * @param {object}    state
   * @param {TimeSync}  data          timesync data
   * @param {Boolean}   addIfMissing  Add to state if not found
   */
  patch: function (state, data, addIfMissing=true) {
    let updated = false
    state.timesync.forEach(item => {
      if (item.id === data.id) {
        item = data
        updated = true
      }
    })

    if (!updated && !addIfMissing) return

    state.timesync.push(data)
  },
  /**
   * Remove a TimeSync
   *
   * @param {object}  state
   * @param {number}  id
   */
  remove: function (state, id) {
    let count = state.timesync.findIndex(item => item.id === id)
    if (count < 0) return
    state.timesync.splice(count, 1)
  }
}
const actions = {
  /**
   * List TimeSync items via API
   *
   * @param {object}  context
   * @param {object}  pageQuery
   * @return {Promise}
   */
  list: function (context, pageQuery) {
    return HTTP.get(TIMESYNC.API.GET, pageQuery)
    .then(({ data }) => {
      context.commit('set', data.data)
      return data.data
    })
  },
  /**
   * Get TimeSync details via API
   *
   * @param {object}  context
   * @param {number}  id
   * @return {Promise}
   */
  get: function (context, id) {
    return HTTP.get(`${TIMESYNC.API.GET}/${id}/`)
    .then(({ data }) => {
      context.commit('patch', data.data)
      return data.data
    })
  },
  /**
   * Post TimeSync details via API
   *
   * @param {object}    context
   * @param {TimeSync}  data
   * @return {Promise}
   */
  post: function (context, data) {
    return HTTP.post(`${TIMESYNC.API.POST}/`, data)
    .then(({ data }) => {
      context.commit('post', data.data)
      return data.data
    })
  },
  /**
   * Patch TimeSync details via API
   *
   * @param {object}    context
   * @param {Number}    id
   * @param {TimeSync}  data
   * @return {Promise}
   */
  patch: function (context, {id, data}) {
    return HTTP.patch(`${TIMESYNC.API.PATCH}/${id}/`, data)
    .then(({ data }) => {
      context.commit('patch', data.data)
      return data.data
    })
  },
  /**
   * Delete TimeSync via API
   *
   * @param {object}  context
   * @param {number}  id
   * @return {Promise}
   */
  remove: function (context, id) {
    return HTTP.remove(`${TIMESYNC.API.DELETE}/${id}/`)
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

