<script>
  export default {
    methods: {
      getObjectByKeyValue (list, field_name, code) {
        return list.find(obj => obj[field_name] === code)
      }
    }
  }
</script>
