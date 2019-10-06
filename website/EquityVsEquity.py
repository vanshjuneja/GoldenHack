import plotly.graph_objects as go
import plotly.io as pyo


class EquityVsEquity(object):
    def __init__(self, equities1, equities2):
        name1 = '</br>2018 Owner\'s</br>Equity'
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=[name1],
            x=[equities1],
            name='2018OwnersEquity',
            orientation='h',
            marker=dict(
                color='#5DADE2',
            ),
            hoverinfo='text'
        ))
        fig.add_trace(go.Bar(
            y=['</br>2019 Owner\'s</br>Equity'],
            x=[equities2],
            name='2019OwnersEquity',
            orientation='h',
            marker=dict(
                color='#FFA500',
            ),
            hoverinfo='text'
        ))

        fig.update_layout(showlegend=False)
        pyo.write_html(fig, file='static/EqVsEq.html', auto_open=False)
