<template>
  <div ref="message-holder" class="messages" :class="appNameLong">
    <div
        v-for="item in items"
        :key="item.id"
        class="mb-2">

      <div class="message"
           :class="item.class">
        <div class="message__row"
             :class="{ 'pr-4': item.closeable }">
          <div class="message__row-content">{{ item.message }}</div>
          <div v-if="item.closeable"
               class="message__row-button"
               @click="$message.remove(item)">
            <cross-icon :class-items="'close'" />
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>

/**
 * @typedef  {object}   Message
 *
 * @property {string}   id            Added on creation
 * @property {string}   message
 * @property {boolean}  closeable
 * @property {number}   timeDelay     Time in seconds
 * @property {number}   timeDisplay   Time in seconds
 */

import crossIcon from '@/assets/cross'

export default {
  name: 'message',

  components: {
    crossIcon
  },

  data () {
    return {
      items: []
    }
  },

  computed: {
    appNameLong () { return process.env.VUE_APP_NAME_FULL || 'BASE' },
    messages () {
      return this.$message.items
    }
  },

  mounted () {
    this.$message.register(this.items)
    document.body.prepend(this.$el)
  },

  beforeDestroy () {
    this.$message.unregister(this.items)
    document.body.removeChild(this.$el)
  },
}
</script>


