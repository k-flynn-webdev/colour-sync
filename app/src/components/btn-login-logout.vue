<template>
  <div>
    <div v-if="isLoggedIn" class="has-text-right">
      <div class="is-uppercase email">{{ userEmail }}</div>
      <a :href="url_logout.href" class="button is-success is-smaller">
        <cross-icon :class-items="'close'" />
      </a>
    </div>

    <a :href="url_login.href" v-else >
      Login
    </a>
  </div>
</template>

<script>
import { LOGIN, LOGOUT, USER, CSRF } from '@/constants'
import crossIcon from '@/assets/cross'
import { genericErrMixin } from '@/plugins/genericErrPlugin'


export default {
  name: 'btn-login-logout',

  components: { crossIcon },

  mixins: [
    genericErrMixin
  ],

  mounted () {
    return this.$store.dispatch(`${CSRF.store}/get`)
    .then(() => this.$store.dispatch(`${USER.store}/get`))
    .catch(err => this.handleError(err))
  },

  data () {
    return {
      url_login: LOGIN.views,
      url_logout: LOGOUT.views,
    }
  },

  computed: {
    userName () {
      return this.$store.state[USER.store].username
    },
    userEmail () {
      return this.$store.state[USER.store].email
    },
    isLoggedIn () {
      return !!this.userEmail
    }
  }
}
</script>
