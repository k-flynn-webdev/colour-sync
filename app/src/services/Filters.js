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

const ITEM_IS_NULL = {
  name: 'itemIsNull',
  filter: function (item, isNull= '--') {
    if (!item) return isNull
    return item
  }
}

const ITEM_LOGIN = {
  name: 'itemLogin',
  filter: function (item, day=true, month=true, year=true, splitChar='/') {
    if (!item) return ''
    if (!item.login_at) return ''

    let result = []

    const dateArr = createDate(item, 'login_at')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join(splitChar)
  }
}

const ITEM_DATE = {
  name: 'itemDate',
  filter: function (item, day=true, month=true, year=true, splitChar='/') {
    if (!item) return ''

    let result = []

    const dateArr = createDate({ date: item }, 'date')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join(splitChar)
  }
}

const ITEM_CREATED = {
  name: 'itemCreated',
  filter: function (item, day=true, month=true, year=true, splitChar='/') {
    if (!item) return ''
    if (!item.createdAt) return ''

    let result = []

    const dateArr = createDate(item, 'createdAt')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join(splitChar)
  }
}


const ITEM_UPDATED = {
  name: 'itemUpdated',
  filter: function (item, day=true, month=true, year=true, splitChar='/') {
    if (!item) return ''
    if (!item.updatedAt) return ''

    let result = []

    const dateArr = createDate(item, 'updatedAt')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join(splitChar)
  }
}

const ITEM_DONE = {
  name: 'itemDone',
  filter: function (item, day=true, month=true, year=true, splitChar='/') {
    if (!item) return ''
    if (!item.done_at) return ''

    let result = []

    const dateArr = createDate(item, 'done_at')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join(splitChar)
  }
}

const ITEM_DELETED = {
  name: 'itemDeleted',
  filter: function (item, day=true, month=true, year=true, splitChar='/') {
    if (!item) return ''
    if (!item.deletedAt) return ''

    let result = []

    const dateArr = createDate(item, 'deletedAt')

    if (day) { result.push(dateArr[0]) }
    if (month) { result.push(dateArr[1]) }
    if (year) { result.push(dateArr[2]) }

    return result.join(splitChar)
  }
}

const ITEM_DATE_ABR = {
  name: 'itemDateAbr',
  filter: function (item) {
    if (!item) return ''
    if (!item.createdAt) return ''

    const dateArr = createDateMonth(item, 'createdAt')

    return `${dateArr[0]} ${dateArr[1]}`
  }
}

const ITEM_TIME_ABR = {
  name: 'itemTimeAbr',
  filter: function (item) {
    if (!item) return ''
    if (!item.createdAt) return ''

    return new Date(item.createdAt).getHours() < 12 ? 'am' : 'pm'
  }
}

const ALL_FILTERS = [
  ITEM_DATE,
  ITEM_CREATED,
  ITEM_UPDATED,
  ITEM_DELETED,
  ITEM_DATE,
  ITEM_IS_NULL,
  ITEM_DATE_ABR,
  ITEM_TIME_ABR
]

export default (Vue) => {
  ALL_FILTERS.forEach(item => Vue.filter(item.name, item.filter))
}
