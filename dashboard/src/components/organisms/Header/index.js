import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import './index.css'

const Header = ({props}) => (
  <div className="header">
    <div className="container">
        <div className="header__wrap">
            <Link to={"/"}>
                <div className="header__logo">
                    <img src="logo.jpeg" alt="Bishkek in photos" />
                </div>
            </Link>
            <div className="header__menu">
            <ul>
                <li>
                    <Link to={'/link'}>
                      Link
                    </Link>
                </li>
                <li>/</li>
                <li>
                    <Link to={'/link'}>
                      Link
                    </Link>
                </li>
                <li>/</li>
                <li>
                    <Link to={'/link'}>
                      Link
                    </Link>
                </li>
                <li>/</li>
                <li>
                    <Link to={'/link'}>
                     Link
                    </Link>
                </li>
            </ul>
            </div>
        </div>
    </div>
  </div>
)

export default Header;