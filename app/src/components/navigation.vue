<template>
  <div class="level is-mobile mb-3">

    <router-link
        :to="{ name: 'home' }"
        class="title has-text-white level-item home">
      {{ $route.meta.title }}
    </router-link>

    <btn-login-logout class="level-right" />
  </div>
</template>

<script>
import btnLoginLogout from '@/components/btn-login-logout'

export default {
  name: 'navigation',

  components: {
    btnLoginLogout,
  }
}
</script>
