<template>
  <b-form @submit.prevent="search">
    <!--SEARCH FIELD-->
    <b-form-group
      id="search-group"
      style="margin-bottom: 0"
      label-for="search"
    >
      <div class="d-flex">
        <b-form-input
          @input="searchInput"
          id="search"
          type="search"
          v-model="searchString"
          :placeholder="$t('table.general.search')"
        ></b-form-input>
        <b-button
          class="ml-1"
          variant="outline-secondary"
          type="submit" >
          <b-icon icon="search"></b-icon>
        </b-button>
      </div>
    </b-form-group>
  </b-form>
</template>

<script>

  export default {
    name: 'SearchField',

    data () {
      return  {
        searchString: null
      }
    },

    methods: {
      searchInput () {
        this.$emit('input', this.searchString)
        if (!this.searchString)
          this.search()
      },

      search () {
        this.$emit('search', this.searchString)
      }
    },
  }
</script>

<style scoped>

</style>
