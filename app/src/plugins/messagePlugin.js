/**
 * @typedef  {object}   Message
 *
 * @property {string}   id            Added on creation
 * @property {string}   message
 * @property {string}   class
 * @property {boolean}  closeable     default = true
 * @property {number}   timeDelay     Time in seconds
 * @property {number}   timeDisplay   Time in seconds, default = 10s
 */
import message from "@/components/message";

const opts = {
  items: []
}

/**
 * Generate a Id string
 *
 * @param {string}    input   Text message input
 * @returns {string}  hash
 */
const generateId = (input) => {
  let hash = 0
  for (let i = 0; i < input.length; ++i)
    hash = (Math.imul(31, hash) + input.charCodeAt(i)) | 0

  return hash
}

/**
 * Add a message to the local stack
 *
 * @param {Message}  msg  Message to create
 * @returns {Boolean}     If a message was created
 */
const createMessage = (msg) => {
  msg.id = generateId(msg.message)
  msg.closeable = msg.closeable || true
  msg.timeDisplay = msg.timeDisplay || 10

  for(let i = 0; i < opts.items.length; i++ ) {
    if (opts.items[i].id === msg.id) return false
  }

  opts.items.push(msg)

  // auto hide
  if (msg.timeDisplay > 0) {
    setTimeout (function () {
      removeMessage(msg)
    }, msg.timeDisplay * 1000)
  }

  return true
}
/**
 * Add a message to be displayed
 *
 * @param {Message}  msg
 */
const addMessage = (msg) => {
  if (msg.timeDelay > 0) {
    const delay = msg.timeDelay
    msg.timeDelay = 0
    return addDelayedMessage(msg, delay)
  }

  createMessage(msg)
}
/**
 * Add a global delayed message to be displayed
 *
 * @param {Message}  msg
 * @param {Number}   delay
 */
const addDelayedMessage = (msg, delay = 1) => {
  setTimeout( function () {
    addMessage(msg)
  }, delay * 1000 + 50)
}
/**
 * Remove message from the local stack
 *
 * @param {Message}   msg
 * @returns {Boolean}       If a message was removed
 */
const removeMessage = (msg) => {
  for (let i = 0, max = opts.items.length; i < max; i++) {
    if (opts.items[i].id === msg.id) {
      opts.items.splice(i,1)
      return true
    }
  }
  return false
}

const MessagePlugin = {
  // install process globally
  install(Vue, options) {

    Vue.component('message', message)

    Vue.prototype.$message = opts

    Vue.prototype.$message.add = addMessage
    Vue.prototype.$message.remove = removeMessage

    Vue.prototype.$message.register = (input) => { opts.items = input }
    Vue.prototype.$message.unregister = (input) => { opts.items = [] }
  }
}

// Automatic installation if Vue has been added to the global scope.
if (typeof window !== 'undefined' && window.Vue) {
  window.Vue.use(MessagePlugin);
}

export default MessagePlugin;