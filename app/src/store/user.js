import Vue from 'vue'
import { USER } from '@/constants';
import HTTP from '@/services/HttpService'


/**
 * Creates a default User Obj
 *
 * @return {User} UserObj
 */
const defaultUserObj = () => {
  return {
    id: -1,
    email: null,
    username: '',
    first_name: null,
    last_name: null,
  }
}

/**
 * Returns initial store state
 *
 * @returns {object}
 */
function initState () {
  return {
    id: -1,
    email: null,
    username: '',
    first_name: '',
    last_name: '',
    full_name: '',
    isLoggedIn: false
  }
}


const mutations = {
  /**
   * Sets the User state
   *
   * @param {object}  state
   * @param {User}    input
   */
  set: function (state, input) {
    Object.entries(input).forEach(([key, value]) => {
      Vue.set(state, key, value)
    })
  }
}
const actions = {
  /**
   * Get User details via API
   *  User must be logged in first `whoami`
   *
   * @param {object}  context
   * @return {Promise}
   */
  get: function (context) {
    return HTTP.get(USER.API.GET)
    .then(({ data }) => {
      context.commit('set', data.data)
      return data.data
    })
  }
}

export default {
  namespaced: true,
  state: initState(),
  mutations: mutations,
  actions: actions
}

/**
 * @typedef {object}    Login
 *
 * @property {string}   email
 * @property {string}   password
 */

/**
 * @typedef {object}    User
 *
 * @property {number}   id
 * @property {string}   email
 * @property {string}   [password]
 * @property {string}   username
 * @property {string}   first_name
 * @property {string}   last_name
 * @property {string}   full_name
 * @property {date}     updated_at
 * @property {date}     created_at
 */

