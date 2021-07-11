# Most likely taken decision after toss
import justpy as jp
import pandas
import datetime
from pytz import utc
chart="""
{
  chart: {
    type: 'bar',
    inverted: false
  },
  title: {
    text: 'Most likely decision taken after toss'
  },
  subtitle: {
    text: ''
  },
  xAxis: {
    categories: [ ],
    crosshair: true
  },
  yAxis: {
    min: 0,
    title: {
      text: ''
    }
  },
  tooltip: {
    headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
    footerFormat: '</table>',
    shared: true,
    useHTML: true
  },
  plotOptions: {
    column: {
      pointPadding: 0,
      borderWidth: 0,
      groupPadding: 0,
      shadow: false
    }
  },
  series: [{
    name: 'Number of Matches',
    data: []
    }]
}
"""
matches = pandas.read_csv('data-set.csv',parse_dates=["date"])

x=['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
    'Rising Pune Supergiant', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Delhi Daredevils', 'Kings XI Punjab',
    'Chennai Super Kings', 'Rajasthan Royals', 'Deccan Chargers',
    'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiants', 'Delhi Capitals']

y = ['SRH','MI','GL','RPS','RCB','KKR','DC','KXIP','CSK','RR','SRH','KTK','PW','RPS','DC']
matches.replace(x,y,inplace = True)

matches_decision = matches.groupby(["toss_decision"]).count()



def app():
    web_page=jp.QuasarPage()
    h1=jp.QDiv(a=web_page,text="IPL ANALYSIS", classes="text-h1 text-center q-pt-lg")
    highchart=jp.HighCharts(a=web_page, options=chart)

    highchart.options.xAxis.categories=list(matches_decision.index)
    highchart.options.series[0].data=list(matches_decision["id"])

    return web_page

jp.justpy(app)
