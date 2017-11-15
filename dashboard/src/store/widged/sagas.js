import {call, put, take, takeEvery, fork} from 'redux-saga/effects'
import axios from 'axios'
import {getInformationSuccess} from './actions'

export function * getInformation() {
  const response = yield call(axios.get, 'http://127.0.0.1:8000/api/v1/user/')
  yield put(getInformationSuccess(response.data))
}
export function * myGetSaga() {
  while (true) {
    const {} = yield take('GET_INFORMATION')
    yield call(getInformation)
  }
}

export default function * () {
  yield fork(myGetSaga)
}
