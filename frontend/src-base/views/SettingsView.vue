<template>
  <div>
    <b-container>
      <head-block :title="$t('title.admin.user_settings')" />
      <b-row class="col-md-10 col-sm-12 col-lg-12 col-12" cols="1" cols-sm="1" cols-md="1" cols-lg="2">
        <b-col class="mb-5"><change-user-data /></b-col>
        <b-col><change-password /></b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
  import HeadBlock from '@base/components/HeadBlock'
  import ChangePassword from '@base/components/settings/ChangePassword'
  import ChangeUserData from '@base/components/settings/ChangeUserData'

  export default {
    name: 'SettingsView',
    components: {
      HeadBlock,
      ChangePassword,
      ChangeUserData
    },
  }
</script>

<style>


</style>
