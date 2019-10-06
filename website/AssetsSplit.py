import plotly.graph_objects as go
import plotly.io as pyo


class AssetsSplit(object):
    def __init__(self, assets, assetsvalues):
        colors = ['#7B241C', '#633974', '#1A5276', '#117864', '#1D8348', '#A93226', '#884EA0', '#2471A3', '#17A589',
                  '#229954', '#F1C40F', '#D98880']

        fig = go.Figure(data=[
            go.Pie(labels=assets,
                   # title='</br>Assets</br>VS</br>Liabilities',
                   titlefont=dict(size=40),
                   values=assetsvalues,
                   hole=.3,
                   text=assets,
                   textposition='inside',
                   textfont=dict(size=30, color='#FFFFFF'),
                   hoverinfo='value+label',
                   marker_colors=colors)])

        pyo.write_html(fig, file='./static/AssetsSplit.html', auto_open=False)
