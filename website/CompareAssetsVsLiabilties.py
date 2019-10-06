import plotly.graph_objects as go
import plotly.io as pyo

class CompareAssetsVsLiabilities(object):
    def __init__(self, assets, liabilties):
        labels = ['Assets', 'Liabilities']
        values = [assets, liabilties]

        fig = go.Figure(data=[
            go.Pie(labels=labels,
                   # title='</br>Assets</br>VS</br>Liabilities',
                   titlefont=dict(size=40),
                   values=values,
                   hole=.3,
                   text=labels,
                   textposition='inside',
                   textfont=dict(size=30, color='#FFFFFF'),
                   hoverinfo='value',
                   marker_colors=['#00A86B', '#B81911'])])

        pyo.write_html(fig, file='static/AssetsVsLiabilities.html', auto_open=False)
