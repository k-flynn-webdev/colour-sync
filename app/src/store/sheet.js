import Vue from 'vue'
import { SHEET } from '@/constants';
import HTTP from '@/services/HttpService'


/**
 * Returns initial store state
 *
 * @returns {object}
 */
function initState () {
  return {
    sheets: []
  }
}

const getters = {
  /**
   * Gets a Sheet from state via ID
   *
   * @param {object}  state
   * @param {number}  id
   * @returns {sheet|void}
   */
  getById: (state) => (id) => {
    return state.sheets.find(item => item.id === id)
  }
}

const mutations = {
  /**
   * Sets the Sheet state
   *
   * @param {object}    state
   * @param {Sheet[]}   input
   */
  set: function (state, input) {
    Vue.set(state, 'sheets', input)
  },
  /**
   * Add a Sheet
   *
   * @param {object}  state
   * @param {Sheet}   data    sheet data
   */
  post: function (state, data) {
    state.sheets.push(data)
  },
  /**
   * Patch a Sheet
   *
   * @param {object}    state
   * @param {Sheet}     data          sheet data
   * @param {Boolean}   addIfMissing  Add to state if not found
   */
  patch: function (state, data, addIfMissing=true) {
    let updated = false

    for(let i= 0, max= state.sheets.length; i < max; i++) {
      if (state.sheets[i].id === data.id) {
        Vue.set(state.sheets, i, data)
        updated = true
      }
    }

    if (!updated && !addIfMissing) return

    state.sheets.push(data)
  },
  /**
   * Remove a Sheet
   *
   * @param {object}  state
   * @param {number}  id
   */
  remove: function (state, id) {
    let count = state.sheets.findIndex(item => item.id === id)
    if (count < 0) return
    state.sheets.splice(count, 1)
  }
}
const actions = {
  /**
   * List Sheets via API
   *
   * @param {object}  context
   * @param {object}  pageQuery
   * @return {Promise}
   */
  list: function (context, pageQuery) {
    return HTTP.get(SHEET.API.GET, pageQuery)
    .then(({ data }) => {
      context.commit('set', data.data)
      return data.data
    })
  },
  /**
   * Get Sheet details via API
   *
   * @param {object}  context
   * @param {number}  id
   * @return {Promise}
   */
  get: function (context, id) {
    return HTTP.get(`${SHEET.API.GET}/${id}/`)
    .then(({ data }) => {
      context.commit('patch', data.data)
      return data.data
    })
  },
  /**
   * Post Sheet details via API
   *
   * @param {object}  context
   * @param {Sheet}  data
   * @return {Promise}
   */
  post: function (context, data) {
    return HTTP.post(`${SHEET.API.POST}/`, data)
    .then(({ data }) => {
      context.commit('post', data.data)
      return data.data
    })
  },
  /**
   * Patch Sheet details via API
   *
   * @param {object}    context
   * @param {Number}    id
   * @param {Sheet}     data
   * @return {Promise}
   */
  patch: function (context, {id, data}) {
    return HTTP.patch(`${SHEET.API.PATCH}/${id}/`, data)
    .then(({ data }) => {
      context.commit('patch', data.data)
      return data.data
    })
  },
  /**
   * Delete Sheet via API
   *
   * @param {object}  context
   * @param {number}  id
   * @return {Promise}
   */
  remove: function (context, id) {
    return HTTP.remove(`${SHEET.API.DELETE}/${id}/`)
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

