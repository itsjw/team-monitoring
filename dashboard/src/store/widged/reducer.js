const information = (state = [], action) => {
  switch (action.type) {
    case 'GET_INFORMATION_SUCCESS':
      return state.concat(action.payload.response)
    default:
      return state
  }
}

export default information
