<template>
  <div id="app"
       class="p-1"
       :class="appNameLong">

    <message />

    <div class="container">

      <navigation />

      <div class="columns is-centered">
        <router-view />
      </div>

    </div>

    <page-footer />

  </div>
</template>

<script>
import navigation from '@/components/navigation'
import pageFooter from '@/components/pageFooter'

export default {
  name: 'app',

  components: {
    navigation,
    pageFooter
  },

  computed: {
    appNameLong () { return process.env.VUE_APP_NAME_FULL || 'BASE' }
  },

}
</script>
