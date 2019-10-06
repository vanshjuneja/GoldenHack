import plotly.graph_objects as go
import plotly.io as pyo


class RevenueVsExpenses(object):
    def __init__(self, revenue, expenses):
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=["Revenue"],
            x=[revenue],
            name='Revenue',
            orientation='h',
            marker=dict(
                color='#5DADE2',
            )
        ))
        fig.add_trace(go.Bar(
            y=['Expenses'],
            x=[expenses],
            name='Expenses',
            orientation='h',
            marker=dict(
                color='#FFA500',
            )
        ))

        pyo.write_html(fig, file='RevenueVsExpenses.html', auto_open=False)
