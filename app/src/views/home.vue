<template>

  <div class="column is-11">
    Enjoy, please sign up

    <router-link :to="{ name: 'project-list' }">
      Projects
    </router-link>
    <router-link :to="{ name: 'sheet-list' }">
      Sheets
    </router-link>
  </div>

</template>

<script>

export default {
  name: 'home',
}
</script>
