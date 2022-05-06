function getData() {
  ajaxGetRequest('/linegraph', linedata)
  ajaxGetRequest('/piechart', piedata)
}
function getBoroData() {
  let inputelement = document.getElementById("boroText")
  let valueToSend = inputelement["value"]
  let toSend = JSON.stringify(valueToSend)
  ajaxPostRequest('/barchart', toSend, bardata)
}
function linedata(response) {
  let data = JSON.parse(response)
  let arrestdates = [
    {
      x: Object.values(data),
      y: Object.keys(data),
      mode: 'lines'
    }
  ]
  return Plotly.newPlot('LineGraph', arrestdates, {
    title: 'Arrests in NYC By Date',
    xaxis: {
      title: '# of Arrests'
    },
    yaxis: {
      title: 'Date'
    }
  })
}
function piedata(response) {
  let data = JSON.parse(response)
  let arrestcounts = [
    {
      x: Object.values(data),
      y: ['The Bronx', 'Brooklyn', 'Queens', 'Manhattan', 'Staten Island'],
      type: 'pie'
    }
  ]
  return Plotly.newPlot('PieChart', arrestcounts, {
    title: 'Arrests Broken Out By Borough'
  })
}
function bardata(response) {
  let data = JSON.parse(response)
  let arrestages = [
    {
      x: Object.values(data),
      y: Object.keys(data),
      mode: 'bar'
    }
  ]
  return Plotly.newPlot('BarChart', arrestages)
}
