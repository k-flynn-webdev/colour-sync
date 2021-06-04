import Vuex from 'vuex'
import sinon from 'sinon'
import { cloneDeep } from 'lodash-es'
import { expect } from 'chai'
import { shallowMount, createLocalVue } from '@vue/test-utils'
import CsrfStore from '@/store/csrf.js'

const localVue = createLocalVue()
localVue.use(Vuex)


// todo more tests
describe('CsrfStore.vue', () => {
  let actions
  let store

  beforeEach(() => {
    const localVue = createLocalVue()
    localVue.use(Vuex)
    store = new Vuex.Store(cloneDeep(CsrfStore))
  })

  it('updating the token also updates the requested_at time', () => {
    expect(store.state.token).to.equal(null)
    expect(store.state.CSRF_requested_at).to.equal(null)
    store.commit('token', 'test')
    expect(store.state.token).to.equal('test')
    expect(new Date(store.state.CSRF_requested_at).toDateString().length).to.above(5)
  })
  it('makes a api call to the csrf endpoint')
  it('if a token was recently requested it should NOT make another call to the csrf endpoint')
})
