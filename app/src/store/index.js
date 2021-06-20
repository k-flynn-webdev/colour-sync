import Vue from 'vue'
import Vuex from 'vuex'
import csrf from './csrf.js'
import user from './user.js'
import project from './project.js'
import sheet from './sheet.js'

Vue.use(Vuex)

const mutations = {}
const getters = {}

export default new Vuex.Store({
  state: {},
  getters: getters,
  mutations: mutations,
  modules: {
    csrf,
    user,
    project,
    sheet
  }
})
