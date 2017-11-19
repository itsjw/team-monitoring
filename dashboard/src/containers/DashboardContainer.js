import React, { Component } from 'react'
import { getInformationRequest } from 'store/actions'
import { connect } from 'react-redux'
import { WidgedList } from 'components'

export const mapStateToProps = state => {
  return {
    information: state.widged.information
  }
}

export const mapDispatchToProps = (dispatch) => ({
  onGet: () => dispatch(getInformationRequest()),
})


export default connect(mapStateToProps, mapDispatchToProps)(WidgedList)
