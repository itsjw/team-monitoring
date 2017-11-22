import React, {Component} from 'react'
import {Graphic} from 'components'
import './index.css'

const Widged = ({props}) => (
  <div className="col-lg-4 col-md-6 col-sm-12 col-xs-12">
    <div style={{
      borderLeft: props.gitlab.commits_per_day>20? '10px solid rgb(0, 253, 55);' : '10px solid red',
      borderRight: props.gitlab.commits_per_day>20? '10px solid rgb(0, 253, 55);' : '10px solid red'
    }} className="widged-item">

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
          <div className="description-text">
           <p>First name: </p>
           <p>{props.first_name}</p>
          </div>
          <div className="description-text">
          <p>Last name: </p>
          <p>{props.last_name}</p>
          </div>
          <div className="description-text">
          <p>Commits per day: </p>
          <p>{props.gitlab.commits_per_day}</p>
          </div>
          <div className="description-text">
          <p>Commits for the week: </p>
          <p>{props.gitlab.commits_per_week}</p>
          </div>
        </div>

      </div>

      <div className="widged-item__content--graphic">
        <Graphic props={props}/>
      </div>

    </div>
  </div>
)

export default Widged;
