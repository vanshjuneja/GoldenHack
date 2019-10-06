import plotly.graph_objects as go
import plotly.io as pyo


class AssetsVsAssets(object):
    def __init__(self, asset1, liabilities1, asset2, liabilities2):
        name1 = str('2018')
        name2 = str('2019')
        fig = go.Figure()
        fig.add_trace(go.Bar(
            y=[name2, name1],
            x=[asset2, asset1],
            name='Assets',
            orientation='h',
            marker=dict(
                color='#0F9D58',
                # line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
            )
        ))
        fig.add_trace(go.Bar(
            y=[name2, name1],
            x=[liabilities2, liabilities1],
            name='Liabilities',
            orientation='h',
            marker=dict(
                color='#DB4437',
                # line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
            )
        ))
        fig.update_yaxes(nticks=4)
        fig.update_layout(barmode='stack')
        pyo.write_html(fig, file='AssetsVsAssets.html', auto_open=True)
