import React, { Component } from 'react'
import './index.css'

const Widged = ({props}) => (
  <div className="col-lg-4 col-md-6 col-sm-12 col-xs-12">
  <div className="widged__item">

    <div className="widged__item-header">
      
      <div className="widged__item-logo">
        <img src={props.avatar_url} alt="" />
      </div>

      <div className="widged__item-nickname">
        <p>Nickname: {props.username}</p>
      </div>

    </div>

    <div className="widged__item-description">

      <div className="widged__item-firstname">
        <p>First name: {props.first_name}</p>
      </div>
      <div className="widged__item-lastname">
        <p>Last name: {props.last_name}</p>
      </div>
      <div className="widged__item-commits">
        <p>Commits per day: {props.gitlab.commits_per_day}</p>
      </div>
      <div className="widged__item-commits--w">
        <p>Commits for the week: {props.gitlab.commits_per_week}</p>
      </div>

    </div>

    <div className="widged__item-graphic">
    </div>

  </div>
  </div>
)

export default Widged;
