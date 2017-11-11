import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import './index.css'

const Footer = () => (
  <div className="footer">
    <div className="container">
        <div className="footer__wrap">
            <Link to={"/"}>
              <div className="footer__logo">
                  <img src="logo.jpeg" alt="Bishkek in photos" />
              </div>
            </Link>
            <div className="footer__map">
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

export default Footer;