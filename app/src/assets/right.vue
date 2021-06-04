<template>
  <svg class="icon"
       :class="classItems"
       viewBox="0 0 512 512"
       xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" xmlns:serif="http://www.serif.com/"
       style="fill-rule:evenodd;clip-rule:evenodd;stroke-linejoin:round;stroke-miterlimit:2;">
    <path d="M428.725,256l-345.45,-234.449l0,468.898l345.45,-234.449Z" />
  </svg>
</template>

<script>
export default {
  name: "right-icon",

  props: {
    classItems: {
      type: String,
      default: ''
    }
  }
}
</script>
