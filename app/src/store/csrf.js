import { CSRF } from '@/constants';
import HTTP from '@/services/HttpService'

const TIME_CHECK = 30 * 60 * 1000; /* ms */

/**
 * Returns initial store state
 *
 * @returns {object}
 */
function initState () {
  return {
    /** @type {null|string} */
    token: null,
     /** @type {date} */
    CSRF_requested_at: null,
  }
}

const mutations = {
  /**
   * Set CSRF token
   *
   * @param {object}  state
   * @param {string}  input
   */
  token: function (state, input) {
    state.token = input
    state.CSRF_requested_at = new Date()
  }
}


const actions = {
  /**
   * Get CSRF token via API
   *
   *  A helper method to try keep requests
   *  legal via a csrf token without spamming the API
   *
   * @param   {object}    context
   * @return  {Promise}   current token value
   */
  get: function (context) {
    if ((context.state.CSRF_requested_at &&
      (new Date() - context.state.CSRF_requested_at) < TIME_CHECK)) {
      return Promise.resolve(context.state.token)
    }

    return HTTP.get(CSRF.API.GET)
    .then(({ data }) => {
      context.commit('token', data.data)
      return data.token
    })
  }
}

export default {
  namespaced: true,
  state: initState(),
  mutations: mutations,
  actions: actions
}