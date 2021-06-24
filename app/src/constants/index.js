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
 * Check Project input is valid
 *
 * @param   {object}    input   Name string to check
 * @returns {boolean}
 */
function checkProject (input) {
  if (!input) return false
  const isNameValid = (input.name && input.name.length >= 5)
  const isMetaValid = (input.meta ? input.meta.length >= 5 : true)
  return (isNameValid && isMetaValid)
}

export const PROJECT = {
  value: 'project',
  store: 'project',
  API: {
    LIST: '/api/project/',
    GET: '/api/project/',
    POST: '/api/project/',
    PATCH: '/api/project',
    DELETE: '/api/project',
  },
  route: { name: 'project', href: '/project' },
  isValid: checkProject,
  init: projectDefaultObj
}

/**
 * @typedef {object}    Project
 *
 * @property {number}   [id]
 * @property {string}   name
 * @property {number}   [owner]
 * @property {string}   meta
 * @property {number}   [sheets]
 * @property {date}     createdAt
 * @property {date}     updatedAt
 * @property {date}     deletedAt
 */

/**
 * Creates a default Project Obj
 *
 * @return {Project} ProjectObj
 */
function projectDefaultObj () {
  return {
    id: -1,
    name: '',
    meta: '',
    owner: undefined,
    sheets: -1,
    createdAt: null,
    updatedAt: null,
    deletedAt: null,
  }
}

/**
 * Check Sheet input is valid
 *
 * @param   {object}    input   Data to check for validation
 * @returns {boolean}
 */
function checkSheet (input) {
  if (!input) return false
  const isNameValid = (input.name && input.name.length >= 5)
  const isMetaValid = (input.meta ? input.meta.length >= 5 : true)
  const isDataValid = (input.data && input.data.length >= 5)
  const isRankingValid = (input.ranking && input.ranking >= 1 && input.ranking <= 999)
  const isURLValid = (input.url && input.url.length >= 5)
  return (isNameValid && isMetaValid && isDataValid && isRankingValid && isURLValid)
}

export const SHEET = {
  value: 'sheet',
  store: 'sheet',
  API: {
    LIST: '/api/sheet/',
    GET: '/api/sheet/',
    POST: '/api/sheet/',
    PATCH: '/api/sheet',
    DELETE: '/api/sheet',
  },
  route: { name: 'sheet', href: '/sheet' },
  isValid: checkSheet,
  init: sheetDefaultObj
}

/**
 * @typedef {object}      Sheet
 *
 * @property {number}     [id]
 * @property {string}     name
 * @property {number}     [owner]
 * @property {number}     project
 * @property {string}     url
 * @property {string}     meta
 * @property {string}     data
 * @property {number}     ranking     range(1 - 999) 999 being strongest
 * @property {date}       createdAt
 * @property {date}       updatedAt
 * @property {date}       deletedAt
 * @property {TimeSync[]} [time_sync_data]
 */

/**
 * Creates a default Sheet Obj
 *
 * @params {number} Project
 * @return {Sheet}  SheetObj
 */
function sheetDefaultObj (project = -1) {
  return {
    id: -1,
    name: '',
    meta: '',
    url: '',
    owner: undefined,
    project: project,
    data: '',
    ranking: 0,
    createdAt: null,
    updatedAt: null,
    deletedAt: null,
  }
}

/**
 * Check TimeSync input is valid
 *
 * @param   {object}    input   Data to check for validation
 * @returns {boolean}
 */
function checkTimeSync (input) {
  // todo
  if (!input) return false
  const isNameValid = (input.name && input.name.length >= 5)
  const isMetaValid = (input.meta ? input.meta.length >= 5 : true)
  const isDataValid = (input.data && input.data.length >= 5)
  const isRankingValid = (input.ranking && input.ranking >= 1 && input.ranking <= 999)
  const isURLValid = (input.url && input.url.length >= 5)
  return (isNameValid && isMetaValid && isDataValid && isRankingValid && isURLValid)
}

export const TIMESYNC = {
  value: 'timesync',
  store: 'timesync',
  API: {
    LIST: '/api/timesync/',
    GET: '/api/timesync/',
    POST: '/api/timesync/',
    PATCH: '/api/timesync',
    DELETE: '/api/timesync',
  },
  route: { name: 'timesync', href: '/timesync' },
  isValid: checkTimeSync,
  init: timeSyncDefaultObj
}

/**
 * @typedef {object}    TimeSync
 *
 * @property {number}   [id]
 * @property {number}   [owner]
 * @property {number}   sheet
 * @property {string}   meta
 * @property {date}     timeStart
 * @property {number}   timeDuration    In days
 * @property {string}   repeatType      Enum (None:NO,Day:DY,Week:WK,Month:MH,Year:YR)
 * @property {number}   repeatVal       In days
 * @property {date}     createdAt
 * @property {date}     updatedAt
 */

/**
 * Creates a default TimeSync Obj
 *
 * @params {number}     Sheet
 * @return {TimeSync}   TimeSyncObj
 */
function timeSyncDefaultObj (sheet = -1) {
  return {
    id: -1,
    owner: undefined,
    meta: '',
    sheet: sheet,
    timeStart: new Date(),
    timeDuration: 7,
    repeatType: 'NO',
    repeatVal: 0,
    createdAt: null,
    updatedAt: null,
  }
}
export const ALL = {
  VARS,
  CSRF,
  USER,
  LOGIN,
  LOGOUT,
  REGISTER,
  PROJECT,
  SHEET
}
