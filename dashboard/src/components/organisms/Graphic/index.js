import React, { Component } from 'react'
import {Doughnut, Line} from 'react-chartjs-2';
import './index.css'

const Graphic = ({props}) => {
  const data = (canvas) => {
		const ctx = canvas.getContext("2d")
    const gradient = ctx.createLinearGradient(0,0,0,150);
    gradient.addColorStop(0, "red");
    gradient.addColorStop(1, "white");
    ctx.fillStyle = gradient;
    ctx.fillRect(10,10,200,150);
    
		return {
      backgroundColor: gradient,
      labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
      datasets: [
        {
          label: 'Commits chart',
          fill: true,
          lineTension: 0,
          backgroundColor: gradient,
          borderColor: 'rgba(0, 0, 0, 0.12);',
          borderCapStyle: 'butt',
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          data: [65, 59, 80, 81, 56, 55, 40]
        }
      ]
		}
	}
 
 
 
 return(
  <div className="graphic__wrap">
     <Line data={data} />
  </div>
 )
}

export default Graphic;
