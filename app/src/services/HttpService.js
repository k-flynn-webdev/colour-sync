import axios from 'axios'
import qs from 'qs'


axios.defaults.headers.common['Accept-Version'] = 'v1'
axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.paramsSerializer = function(params) {
  return qs.stringify(params,
  { encode: false })
};

axios.interceptors.response.use(httpSuccess, httpError)

;(function init () {
  // auto http code here
})()

function authSet (auth) {
  // set json token here
}

function authRemove () {
  // remove json token here
}


function httpSuccess (res) {
  return res
}

function httpError (err) {
  throw err
}

function get (url, params) {
  return axios.get(url, params)
}

function post (url, params) {
  return axios.post(url, params)
}

function put (url, params) {
  return axios.put(url, params)
}

function patch (url, params) {
  return axios.patch(url, params)
}

function remove (url, params) {
  return axios.delete(url, params)
}

const services = {
  get,
  post,
  put,
  patch,
  remove,
  authSet,
  authRemove,
}
export default services
