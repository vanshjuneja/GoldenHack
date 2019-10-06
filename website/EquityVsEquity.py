import plotly.graph_objects as go
import plotly.io as pyo


class EquityVsEquity(object):
    def __init__(self, equities1, equities2):
        name1 = '2018</br>Owners</br>Equity'
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=[name1],
            x=[equities1],
            name='2018OwnersEquity',
            orientation='h',
            marker=dict(
                color='#5DADE2',
            )
        ))
        fig.add_trace(go.Bar(
            y=['2019</br>Owners</br>Equity'],
            x=[equities2],
            name='2019OwnersEquity',
            orientation='h',
            marker=dict(
                color='#FFA500',
            )
        ))
        fig.update_layout(showlegend=False)
        pyo.write_html(fig, file='static/EquitiesVsEquities.html', auto_open=False)
