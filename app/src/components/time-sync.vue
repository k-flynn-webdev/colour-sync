<template>
  <div>

    <div v-if="short" class="short span-comma">
      <span class="id">[{{ timeSync.id }}]</span>
      <span class="meta">{{ timeSync.meta }}</span>
      <span class="date">{{ timeSync.date | itemDate }}</span>
      <span class="duration-type">{{ timeSync.durationType }}</span>
      <span class="duration-val">{{ timeSync.durationVal }}</span>
    </div>

    <div v-if="update" class="span-comma">
      <span class="id">[{{ timeSync.id }}]</span>
      <span class="meta">{{ timeSync.meta }}</span>
      <span class="date">{{ timeSync.date | itemDate }}</span>
      <span class="duration-type">{{ timeSync.durationType }}</span>
      <span class="duration-val">{{ timeSync.durationVal }}</span>
      <span class="created-at">{{ timeSync.createdAt | itemDate }}</span>
      <span class="updated-at">{{ timeSync.updatedAt | itemDate }}</span>
    </div>

  </div>
</template>

<script>
import { TIMESYNC } from '@/constants'
import crossIcon from '@/assets/cross'
import { genericErrMixin } from '@/plugins/genericErrPlugin'


export default {
  name: 'time-sync',

  components: { crossIcon },

  mixins: [
    genericErrMixin
  ],

  props: {
    /** @type {Boolean} Show a short non-interactive object */
    short: {
      required: false,
      default: false,
      type: Boolean
    },
    /** @type {Boolean} Allow TimeSync to be updated */
    update: {
      required: false,
      default: false,
      type: Boolean
    },
    /** @type {TimeSync} */
    timeSync: {
      required: true,
      type: Object
    }
  },

  data () {
    return {
    }
  },

  computed: {
  },

  methods: {
  }
}
</script>
