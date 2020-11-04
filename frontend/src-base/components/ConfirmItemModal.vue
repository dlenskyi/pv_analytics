<template>
  <div>
    <b-modal
      :title="title"
      :ok-title="okButtonTitle"
      :cancel-title="cancelButtonTitle"
      :id="modalId"
      @ok="onConfirm">
      <p class="my-4">{{ text }}</p>
    </b-modal>
  </div>
</template>

<script>


  export default {
    name: 'ConfirmItemModal',

    data () {
      return {
      }
    },

    props: {
      title: {
        type: String,
        required: true
      },
      text: {
        type: String,
        required: true
      },
      okButtonTitle: {
        type: String,
        required: true
      },
      cancelButtonTitle: {
        type: String,
        required: true
      },
      modalId: {
        type: String,
        required: true
      }
    },

    methods: {
      onConfirm () {
        this.$emit('onConfirm')
      }
    }
  }
</script>

<style>

</style>
