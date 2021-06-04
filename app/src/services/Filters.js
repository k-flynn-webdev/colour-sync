const createDate = (item, field) => {
  const newDate = new Date(item[field])
  const Day = newDate.getDate()
  const Month = newDate.getMonth() + 1
  const Year = newDate.getFullYear()

  return [Day, Month, Year ]
}

const MONTHS = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]

const createDateMonth = (item, field) => {
  const newDate = new Date(item[field])
  const Day = newDate.getDate()
  const Month = MONTHS[newDate.getMonth()]

  return [Day, Month]
}

const ITEM_LOGIN = {
  name: 'itemLogin',
  filter: function (item, day=true, month=true, year=true) {
    if (!item) return ''
    if (!item.login_at) return ''

    let result = []

    const dateArr = createDate(item, 'login_at')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join('/')
  }
}

const ITEM_UPDATE = {
  name: 'itemUpdate',
  filter: function (item, day=true, month=true, year=true) {
    if (!item) return ''
    if (!item.updated_at) return ''

    let result = []

    const dateArr = createDate(item, 'updated_at')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join('/')
  }
}

const ITEM_DATE = {
  name: 'itemDate',
  filter: function (item, day=true, month=true, year=true) {
    if (!item) return ''
    if (!item.created_at) return ''

    let result = []

    const dateArr = createDate(item, 'created_at')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join('/')
  }
}

const ITEM_DONE = {
  name: 'itemDone',
  filter: function (item, day=true, month=true, year=true) {
    if (!item) return ''
    if (!item.done_at) return ''

    let result = []

    const dateArr = createDate(item, 'done_at')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join('/')
  }
}

const ITEM_DATE_ABR = {
  name: 'itemDateAbr',
  filter: function (item) {
    if (!item) return ''
    if (!item.created_at) return ''

    const dateArr = createDateMonth(item, 'created_at')

    return `${dateArr[0]} ${dateArr[1]}`
  }
}

const ITEM_TIME_ABR = {
  name: 'itemTimeAbr',
  filter: function (item) {
    if (!item) return ''
    if (!item.created_at) return ''

    return new Date(item.created_at).getHours() < 12 ? 'am' : 'pm'
  }
}

const ALL_FILTERS = [
  ITEM_DATE,
  ITEM_DATE_ABR,
  ITEM_TIME_ABR
]

export default (Vue) => {
  ALL_FILTERS.forEach(item => Vue.filter(item.name, item.filter))
}
