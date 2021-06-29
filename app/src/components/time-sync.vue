<template>
  <div class="time-sync">

    <div v-if="short" class="short span-comma">
      <span class="id">[{{ timeSync.id }}]</span>
      <span class="meta">{{ timeSync.meta }}</span>
      <span class="date">{{ timeSync.date | itemDate }}</span>
      <span class="duration-type">{{ timeSync.durationType }}</span>
      <span class="duration-val">{{ timeSync.durationVal }}</span>
    </div>

    <form v-if="update" class="span-comma">
      <div class="field is-horizontal">
        <div class="field-label is-normal">
          <label class="label">ID[{{ timeSync.id }}]</label>
        </div>
        <div class="field-body">

          <div class="field">
            <p class="control">
              <input
                  v-model="timeSync.meta"
                  class="input"
                  type="text"
                  placeholder="Meta">
            </p>
          </div>

          <div class="field has-addons">
            <div class="control">
              <div class="select">
                <select v-model="timeSync.durationType">
                  <option
                      v-for="(option, key) in optionsDuration"
                      :key="key"
                      :value="key">
                    {{ option }}
                  </option>
                </select>
              </div>
            </div>
            <p class="control is-expanded">
              <input
                  v-model="timeSync.durationVal"
                  class="input"
                  type="number"
                  step="1"
                  min="1"
                  max="365"
                  placeholder="7">
            </p>
          </div>

        </div>

        <div class="field">
          <label class="control">
            Date
            <input
                v-model="timeSync.date"
                class="input"
                type="datetime-local"
            >
          </label>
        </div>

      </div>

      <span class="created-at">{{ timeSync.createdAt | itemDate }}</span>
      <span class="updated-at">{{ timeSync.updatedAt | itemDate }}</span>
    </form>

  </div>
</template>

<script>
import { TIMESYNC, REPEAT_CHOICES, DURATION_CHOICES } from '@/constants'
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
    optionsDuration () { return DURATION_CHOICES },
    optionsRepeat () { return REPEAT_CHOICES }
  },

  methods: {
  }
}
</script>
