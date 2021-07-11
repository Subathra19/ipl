# Most likely taken decision after toss
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
        text: 'Total Runs per Season'
    },
    subtitle: {
        text: ' '
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Year'
        },
        labels: {
            format: '{value}'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Total Runs'
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
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Total Runs',
        data: [[0, 0], [0, 0]]
    }]
}
"""
matches = pandas.read_csv('data-set.csv',parse_dates=["date"])
runs = pandas.read_csv('runs.csv')

x=['Sunrisers Hyderabad', 'Mumbai Indians', 'Gujarat Lions',
    'Rising Pune Supergiant', 'Royal Challengers Bangalore',
    'Kolkata Knight Riders', 'Delhi Daredevils', 'Kings XI Punjab',
    'Chennai Super Kings', 'Rajasthan Royals', 'Deccan Chargers',
    'Kochi Tuskers Kerala', 'Pune Warriors', 'Rising Pune Supergiants', 'Delhi Capitals']

y = ['SRH','MI','GL','RPS','RCB','KKR','DC','KXIP','CSK','RR','SRH','KTK','PW','RPS','DC']
matches.replace(x,y,inplace = True)
runs.replace(x,y,inplace = True)

new_data=pandas.merge(matches,runs, on='id')
new_data['season'] = new_data['date'].dt.year
runs_season=new_data.groupby(["season"]).sum()

#avgruns_each_season=new_data.groupby(['season']).count().id.reset_index()
#avgruns_each_season.rename(columns={'id':'matches'},inplace=1)
#avgruns_each_season['total_runs']=runs_season['total_runs']
#avgruns_each_season['average_runs_per_match']=avgruns_each_season['total_runs']/avgruns_each_season['matches']
#avgruns_each_season


def app():
    web_page=jp.QuasarPage()
    h1=jp.QDiv(a=web_page,text="IPL ANALYSIS", classes="text-h1 text-center q-pt-lg")
    highchart=jp.HighCharts(a=web_page, options=chart)


    highchart.options.xAxis.categories=list(runs_season.index)
    highchart.options.series[0].data=list(runs_season["total_runs"])

    return web_page

jp.justpy(app)
