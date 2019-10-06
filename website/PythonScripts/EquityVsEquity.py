import plotly.graph_objects as go
import plotly.io as pyo


class EquityVsEquity(object):
    def __init__(self, equities1, equities2):
        name1 = 'Previous Year Equities'
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=[name1],
            x=[equities1],
            name='Previous Year Equities',
            orientation='h',
            marker=dict(
                color='#5DADE2',
            )
        ))
        fig.add_trace(go.Bar(
            y=['Current Year Equities'],
            x=[equities2],
            name='Current Year Equities',
            orientation='h',
            marker=dict(
                color='#FFA500',
            )
        ))

        pyo.write_html(fig, file='EquitiesVsEquities.html', auto_open=False)
