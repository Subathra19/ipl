# Winning percentage
import justpy as jp
import pandas
import datetime
from pytz import utc

chart="""
{
    chart: {
        type: 'bar'
    },
    title: {
        text: 'Match Played, Wins And Win Percentage'
    },
    subtitle: {
        text: ' '
    },
    xAxis: {
        categories: [ ],
        title: {
            text: null
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Count',
            align: 'high'
        },
        labels: {
            overflow: 'justify'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' '
    },
    plotOptions: {
        bar: {
            dataLabels: {
                enabled: true
            }
        }
    },
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'top',
        x: 40,
        y: 80,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF',
        shadow: true
    },
    credits: {
        enabled: false
    },
    series: [{
        name: ' ',
        data: [ ]
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

matches_played=pandas.concat([matches['team1'],matches['team2']])
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=['Team','Total Matches']
matches_played['Wins']=matches['winner'].value_counts().reset_index()['winner']
matches_played["Percentage"]=round(matches_played['Wins']/matches_played['Total Matches'],3)*100

def app():
    web_page=jp.QuasarPage()
    h1=jp.QDiv(a=web_page,text="IPL ANALYSIS", classes="text-h1 text-center q-pt-lg")
    highchart=jp.HighCharts(a=web_page, options=chart)

    highchart.options.xAxis.categories=list(matches_played["Team"])
    #highchart.options.series[0].data=list(matches_count["result"])
    
    hc_data=[{"name":value , "data":[data_value for data_value in matches_played[value]]} for value in ['Total Matches','Wins','Percentage']]
    highchart.options.series=hc_data
    return web_page

jp.justpy(app)
