import React, {Component} from 'react'
import {Doughnut, Line} from 'react-chartjs-2';
import './index.css'

const Graphic = ({props}) => {
  const data = (canvas) => {
    const ctx = canvas.getContext("2d")
    const gradient = ctx.createLinearGradient(0, 0, 0, 150);
    gradient.addColorStop(0, "green");
    gradient.addColorStop(1, "white");
    ctx.fillStyle = gradient;
    ctx.fillRect(10, 10, 200, 150);
    var today = new Date();
    var Mo = 0;
    var Tu = 0;
    var We = 0;
    var Th = 0;
    var Fr = 0;
    var date2
    const date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
    function dd(d){
      return date2 = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + (today.getDate()+d);
    }

    if(date == dd(0)){
      Mo = props.gitlab.commits_per_day
    }else if(date == dd(1)){
      Tu = props.gitlab.commits_per_day
    }else if(date == dd(2)){
      We = props.gitlab.commits_per_day
    }else if(date == dd(3)){
      Th = props.gitlab.commits_per_day
    }else if(date == dd(4)){
      Fr = props.gitlab.commits_per_day
    }
    
    return {
      backgroundColor: gradient,
      labels: [
        'Mo',
        'Tu',
        'We',
        'Th',
        'Fr'
      ],
      datasets: [
        {
          label: 'Commits',
          fill: true,
          lineTension: 0,
          backgroundColor: gradient,
          borderColor: 'rgba(0, 0, 0, 0.12);',
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(0, 0, 0, 0.12);',
          pointBackgroundColor: '#fff',
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          data: [
            Mo,
            Tu,
            We,
            Th,
            Fr
          ]
        }
      ]
    }
  }

  return (<Line data={data}/>)
}

export default Graphic;
