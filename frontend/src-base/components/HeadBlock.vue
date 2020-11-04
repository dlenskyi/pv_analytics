<template>
  <section id="head">
    <h1 class="uppercase">
      <slot name="title">{{ title }}</slot>
    </h1>
  </section>
</template>

<script>

  export default {
    name: 'HeadBlock',

    props: {
      title: {
        type: String,
        required: true,
      }
    },

    data () {
      return  {
      }
    },
  }
</script>

<style scoped>

</style>
