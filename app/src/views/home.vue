<template>

  <div class="column is-11">
    Enjoy, please sign up

    <router-link :to="{ name: 'project-create' }">
      Projects
    </router-link>
  </div>

</template>

<script>

export default {
  name: 'home',
}
</script>
