export const VARS = {
  name: process.env.APP_NAME_SHORT || 'BASE',
  pageCount: 20,
}

export const SORT_OPTIONS = {
  value: 'sort',
  store: null,
  direction: {
    asc: { label: 'asc', value: 1 },
    desc: { label: 'desc', value: -1 }
  },
  options: {
    created: { label: 'created', value: 'created_at' },
    updated: { label: 'updated', value: 'updated_at' },
    deleted: { label: 'deleted', value: 'deleted_at' },
  },
}

export const CSRF = {
  value: 'csrf',
  store: 'csrf',
  API: {
    GET: '/api/csrf/',
  }
}

/**
 * Check Email input is valid
 *
 * @param   {string}    input   Email string to check
 * @returns {boolean}
 */
function checkEmail (input) {
  return (input &&
      input.split('@').length > 1 &&
      input.split('.').length > 1)
}

/**
 * Check Password input is valid
 *
 * @param   {string}    input   Password string to check
 * @returns {boolean}
 */
function checkPassword (input) {
  return (input && input.length >= 8)
}

export const REGISTER = {
  value: 'signup',
  route: { name: 'signup', href: '/accounts/signup' },
  API: {
    GET: '/accounts/signup',
    POST: '/accounts/signup'
  },
  isValid: (input) => {
    return (input &&
        input.email &&
        input.password &&
        checkEmail(input.email) &&
        checkPassword(input.password))
  }
}

export const LOGIN = {
  value: 'login',
  route: { name: 'login', href: '/accounts/login/' },
  API: {
    GET: '/accounts/login',
    POST: '/accounts/login'
  },
  isValid: REGISTER.isValid
}

export const LOGOUT = {
  value: 'logout',
  route: { name: 'logout', href: '/accounts/logout/' },
  API: {
    GET: '/accounts/logout',
    POST: '/accounts/logout'
  }
}

/**
 * Used to get current logged in users details directly from the server API
 */
export const USER = {
  value: 'user',
  store: 'user',
  cookie: 'user-local',
  API: {
    GET: '/api/whoami/'
  }
}

export const ADMIN = {
  value: 'admin',
  store: 'admin',
  route: { name: 'admin', href: '/accounts/admin/' },
}

/**
 * @typedef {object}    Track
 *
 * @property {number}   id
 * @property {number}   user
 * @property {string}   track
 * @property {Tag[]}    tags
 * @property {date}     created_at
 * @property {date}     updated_at
 */

export const ALL = {
  VARS,
  CSRF,
  USER,
  LOGIN,
  LOGOUT,
  REGISTER,
}
