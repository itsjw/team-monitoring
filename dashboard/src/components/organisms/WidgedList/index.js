import React, {Component} from 'react'
import {Widged} from 'components'
import './index.css'

class WidgedList extends Component {
  componentWillMount() {
    this.props.onGet()
  }
  render() {
    console.log(this.props)
    return (
      <div className="widged-list">
        <div className="container">
          <div className="widged-list__wrapp">
            {
              this.props.information.map(info => {
                return <Widged key={info.id} props={info}/>
              })
            }
          </div>
        </div>
      </div>
    )
  }
}

export default WidgedList;
