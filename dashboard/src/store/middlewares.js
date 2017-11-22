const { middleware: thunkMiddleware } = require('redux-saga-thunk')
import { createLogger } from "redux-logger";

const logger = createLogger()

const req = require.context('.', true, /\.\/.+\/middleware\.js$/)

module.exports = req.keys()
  .map(key => req(key).default)
  .concat([
    thunkMiddleware,
    logger
  ])
