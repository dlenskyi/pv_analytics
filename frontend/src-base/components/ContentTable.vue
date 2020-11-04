<template>
  <div>
    <b-table
      striped
      hover
      responsive
      bordered
      :sticky-header="stickyHeaderHeight"
      :primary-key="primaryKey"
      :tbody-transition-props="transProps"
      head-variant="dark"
      :sort-by.sync="sortBy"
      :sort-desc.sync="sortDesc"
      :items="items"
      @row-clicked="onRowCLick"
      :class="tableClass"
      :tbody-tr-class="tbodyTrClass"
      :fields="fields">
      <template v-slot:[`cell(${slot.field})`]="row" v-for="slot in slots">
        <slot :name="slot.name" :tbl="row"></slot>
      </template>
      <template v-slot:[defaultSlot.name]="row" v-for="defaultSlot in defaultSlots">
        <slot :name="defaultSlot.name" :tbl="row"></slot>
      </template>
    </b-table>
  </div>
</template>

<script>

  export default {
    name: 'ContentTable',

    data () {
      return {
        sortBy: this.defaultSortBy,
        sortDesc: this.defaultSortDesc,
      }
    },

    props: {
      fields: {
        type: Array,
        required: true
      },
      items: {
        type: Array,
        required: true
      },
      slots: {
        type: Array,
        default: () => []
      },
      defaultSlots: {
        type: Array,
        default: () => []
      },
      transProps: {
        type: Object,
        default: () => {}
      },
      primaryKey: {
        type: String,
        default: ''
      },
      defaultSortBy: {
        type: String,
        default: ''
      },
      defaultSortDesc: {
        type: Boolean,
        default: false
      },
      tbodyTrClass: {
        required: false
      },
      tableClass: {
        type: String,
        required: false
      },
      stickyHeaderHeight: {
        type: String,
        required: false
      }
    },

    methods: {
      onRowCLick (data, index, event) {
        this.$emit('row-clicked', data, event)
      }
    }
  }
</script>

<style>

</style>
