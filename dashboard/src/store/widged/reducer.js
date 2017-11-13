const information = (state = {
  information: []
}, action) => {
  switch (action.type) {
    case 'GET_INFORMATION_SUCCESS':
      return Object.assign({}, state, action.payload.response)
    default:
      return state
  }
}

export default information
