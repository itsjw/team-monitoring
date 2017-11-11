import React, { Component } from 'react'
import { Widged } from 'components'
import './index.css'

class WidgetList extends Component {
  componentWillMount() {
    this.props.onGet()
  }
  render(){
    return (
      <div className="widged-list">
        <div className="container">
          <div className="widged-list__wrapp">
            {this.props.information.map(info => {
              return <Widged key={info.id} props={info} />
            })}
          </div>
        </div>
      </div>
    )
  }
}

export default WidgetList;
