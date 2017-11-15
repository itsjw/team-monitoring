const information = (state = {information: []}, action) => {
  switch (action.type) {
    case 'GET_INFORMATION_SUCCESS':
    console.log(action)
      return Object.assign({}, state, {information: action.payload.response})
    default:
      return state
  }
}

export default information
