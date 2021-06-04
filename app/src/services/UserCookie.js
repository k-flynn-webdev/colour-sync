import { USER } from '@/constants'

/**
 * Get local storage of a user model
 */
function getCookie() {
  return localStorage.getItem(USER.cookie)
}

/**
 * Save raw User to local storage as a user model in JSON
 *
 * @param {object} input
 */
function saveCookie(input) {
  if (!input) {
    removeCookie()
    return
  }
  localStorage.setItem(USER.cookie, JSON.stringify(input))
}

/**
 * Remove local storage of a user model
 */
function removeCookie() {
  localStorage.removeItem(USER.cookie)
}

export default {
  get: getCookie,
  save: saveCookie,
  remove: removeCookie
}
