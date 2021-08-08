/**
 * @typedef {object}    ItemConfig    An object config to track a number of related things to an item
 *
 * @property {string}   value     api name
 * @property {string}   store     store name
 * @property {string}   route     route name
 * @property {object}   API       api endpoints {list, get, post, patch, delete}
 * @property {object}   views     view names and `props` required {list, view, create, update}
 * @property {function} isValid   check if a object is valid to create the item
 * @property {function} init      create a item
 *
 * @returns {Object}
 */


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

export const LOGIN = {
  value: 'login',
  views: { href: '/accounts/login/' },
}

export const REGISTER = {
  value: 'signup',
  views: { href: '/accounts/signup' },
}

export const LOGOUT = {
  value: 'logout',
  views: { href: '/accounts/logout/' },
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
  views: { href: '/accounts/admin/' },
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
  const isURLValid = (input.url ? input.url.length >= 4 : true)
  const isMetaValid = (input.meta ? input.meta.length >= 5 : true)
  return (isNameValid && isMetaValid)
}

/** @type {ItemConfig} Project */
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
  views: {
    list: { name: 'project-list' },
    view: { name: 'project-view', props: ['projectId'] },
    create: { name: 'project-create' },
  },
  isValid: checkProject,
  init: createProjectObj
}

/**
 * @typedef {object}    Project
 *
 * @property {number}   [id]
 * @property {string}   name
 * @property {string}   url
 * @property {string}   meta
 * @property {number}   [sheets]
 * @property {number}   [owner]
 * @property {date}     createdAt
 * @property {date}     updatedAt
 * @property {date}     deletedAt
 */

/**
 * Creates a Project Obj
 *
 * @return {Project} ProjectObj
 */
function createProjectObj () {
  return {
    id: -1,
    name: '',
    url: '',
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

/** @type {ItemConfig} Sheet */
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
  views: {
    list: { name: 'sheet-list', props: ['projectId'] },
    view: { name: 'sheet-view', props: ['sheetId'] },
    create: { name: 'sheet-create', props: ['projectId'] },
  },
  isValid: checkSheet,
  init: createSheetObj
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
 * Creates a Sheet Obj
 *
 * @params {number} Project
 * @return {Sheet}  SheetObj
 */
function createSheetObj (project = -1) {
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
  // TODO
  if (!input) return false
  const isNameValid = (input.name && input.name.length >= 5)
  const isMetaValid = (input.meta ? input.meta.length >= 5 : true)
  const isDataValid = (input.data && input.data.length >= 5)
  const isRankingValid = (input.ranking && input.ranking >= 1 && input.ranking <= 999)
  const isURLValid = (input.url && input.url.length >= 5)
  return (isNameValid && isMetaValid && isDataValid && isRankingValid && isURLValid)
}

/** @type {ItemConfig} TimeSync */
export const TIMESYNC = {
  value: 'time',
  store: 'time',
  API: {
    LIST: '/api/time/',
    GET: '/api/time/',
    POST: '/api/time/',
    PATCH: '/api/time',
    DELETE: '/api/time',
  },
  views: {
    list: { name: 'time-list', props: ['sheetId'] },
    view: { name: 'time-view', props: ['timeId'] },
    create: { name: 'time-create', props: ['sheetId'] },
  },
  isValid: checkTimeSync,
  init: createTimeSyncObj
}

/**
 * @typedef {object}    TimeSync
 *
 * @property {number}   [id]
 * @property {number}   [owner]
 * @property {number}   sheet
 * @property {string}   meta
 * @property {date}     date            Date becomes active (1st occurrence)
 * @property {number}   durationVal     In days, default is 7 days
 * @property {string}   durationType    Enum Opts: (None:NO,Day:DY,Week:WK,Month:MH,Year:YR), default is ON
 * @property {date}     createdAt
 * @property {date}     updatedAt
 */

/**
 * Creates a TimeSync Obj
 *
 * @params {number}     Sheet
 * @return {TimeSync}   TimeSyncObj
 */
function createTimeSyncObj (sheet = -1) {
  return {
    id: -1,
    owner: undefined,
    meta: '',
    sheet: sheet,
    date: new Date().toISOString().split('T')[0],
    durationType: 'ON',
    durationVal: 7,
    createdAt: null,
    updatedAt: null,
  }
}

export const DURATION_CHOICES = {
  ON: 'Active',
  DY: 'Day',
  WK: 'Week',
  MH: 'Month',
  YR: 'Year',
}
export const REPEAT_CHOICES = {
  NO: 'None',
  DY: 'Day',
  WK: 'Week',
  MH: 'Month',
  YR: 'Year',
}





export const ALL = {
  VARS,
  CSRF,
  USER,
  LOGIN,
  LOGOUT,
  REGISTER,
  PROJECT,
  SHEET,
  TIMESYNC,
}
