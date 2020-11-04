<script>
  import moment from 'moment'
  import { DATE_FORMAT } from '@base/configs'

  export default {
    methods: {
      formatNumber (number, precision) {
        if (number) {
          return Number(number).toLocaleString(
            // eslint-disable-next-line no-undef
            LANGUAGE_CODE, {minimumFractionDigits: precision}
          )
        }
        return ''
      },

      formatDate (rawDate) {
        return moment(rawDate).format(DATE_FORMAT)
      }
    }
  }
</script>
