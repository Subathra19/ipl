# Stadiums vs Matches
import justpy as jp
import pandas
import datetime
from pytz import utc
chart="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Stadiums vs Matches'
    },
    subtitle: {
        text: ' '
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Stadium'
        },
        labels: {
            format: '{value}'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Number of Matches'
        },
        labels: {
            format: '{value}'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} : {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'name',
        data: [[0, 0], [0, 0]]
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

matches_stadium=matches.groupby(["venue"]).count()


def app():
    web_page=jp.QuasarPage()
    h1=jp.QDiv(a=web_page,text="IPL ANALYSIS", classes="text-h1 text-center q-pt-lg")
    highchart=jp.HighCharts(a=web_page, options=chart)

    highchart.options.xAxis.categories=list(matches_stadium.index)
    highchart.options.series[0].data=list(matches_stadium["result"])

    return web_page

jp.justpy(app)
