export function getInformationRequest() {
  return {
    type: 'GET_INFORMATION',
  }
}
export function getInformationSuccess(response) {
  return {
    type: 'GET_INFORMATION_SUCCESS',
    payload: {
      response
    }
  }
}
