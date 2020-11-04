<script>
  export default {
    methods: {
      getTotal (list, field_name) {
        return list.reduce(function(total, item) {
          return total + Number(item[field_name])
        }, 0)
      }
    }
  }
</script>
