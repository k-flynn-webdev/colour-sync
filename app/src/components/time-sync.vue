<template>
  <div>
    <div v-if="!update" class="span-comma">
      <span class="id">[{{ timeSync.id }}]</span>
      <span class="meta show-on-hover">{{ timeSync.meta }}</span>
      <span class="time-start">{{ timeSync.timeStart | itemDate }}</span>
      <span class="time-duration">{{ timeSync.timeDuration }}</span>
      <span class="repeat-type">{{ timeSync.repeatType }}</span>
      <span class="repeat-val">{{ timeSync.repeatVal }}</span>
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
    /** @type {Boolean} Allow TimeSync to be created */
    create: {
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
    /** @type {Boolean} Allow TimeSync to be deleted */
    remove: {
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
