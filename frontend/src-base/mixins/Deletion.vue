<script>
  export default {
    methods: {
      deleteObject (obj) {
        this.selectedObject = obj
        this.$bvModal.show('delete-item')
      },
      confirmDeleteObject (
        deleteAction,
        idFieldName,
        deleteSuccessMessage,
        modalId,
      ) {
        // Confirm the deletion of an object
        //
        // deleteAction: the action that is going to be dispatched
        //
        // idFieldName: the name of the selectedObject key that
        // contains the ID
        //
        // deleteSuccessMessage: the message that is displayed
        // on success
        //
        // modalId: the ID of the modal window that should be
        // hidden on success
        if (this.loading)
          return
        this.loading = true
        this.loader = this.$loading.show(this.$_loaderOptions)
        this.$store.dispatch(deleteAction, this.selectedObject[idFieldName])
          .then(() => {
            this.$emit('objectDeleted')
            if (modalId) {
              this.$nextTick(() => {
                this.$bvModal.hide(modalId)
              })
            }
            this.$notify({
              group: 'app',
              type: 'success',
              title: this.$t('notifications.title.success'),
              text: deleteSuccessMessage
            })
          })
          .catch((error) => {
            this.$_notifyError(error.response, this)
          })
          .finally(() => {
            this.loader.hide()
            this.loading = false
          })
      },
    }
  }
</script>
