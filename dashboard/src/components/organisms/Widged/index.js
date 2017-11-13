import React, {Component} from 'react'
import {Graphic} from 'components'
import './index.css'

const Widged = ({props}) => (
  <div className="col-lg-4 col-md-6 col-sm-12 col-xs-12">
    <div className="widged-item">

      <div className="widged-item__header">

        <div className="widged-item__header--logo">
          <img src={props.avatar_url} alt=""/>
        </div>

        <div className="widged-item__header--description">
          <p>{props.username}</p>
          <p>{props.last_name} {props.first_name}</p>
        </div>

      </div>

      <div className="widged-item__content">

        <div className="widged-item__content--description">
          <p>First name: {props.first_name}</p>
          <p>Last name: {props.last_name}</p>
          <p>Commits per day: {props.gitlab.commits_per_day}</p>
          <p>Commits for the week: {props.gitlab.commits_per_week}</p>
        </div>

      </div>

      <div className="widged-item__content--graphic">
        <Graphic/>
      </div>

    </div>
  </div>
)

export default Widged;
