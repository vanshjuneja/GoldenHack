import plotly.graph_objects as go
import plotly.io as pyo


class RevenueVsRevenue(object):
    def __init__(self, revenue1, revenue2, target1, target2):
        fig = go.Figure()

        range1 = target2 * 0.6
        range2 = target2 * 0.8
        rangex = max(revenue2, target2) * 1.1
        ref = target2
        fig.add_trace(go.Indicator(
            mode="number+gauge+delta",
            value=revenue2,
            delta={'reference': revenue1},
            domain={'x': [0.25, 1], 'y': [0.4, 0.6]},
            title={'text': "2019 Revenue ($CAD)"},
            gauge={
                'shape': "bullet",
                'axis': {'range': [None, rangex]},
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': target2},
                'steps': [
                    {'range': [0, range1], 'color': "gray"},
                    {'range': [range1, range2], 'color': "lightgray"}],
                'bar': {'color': "black"}}))

        range1 = target1 * 0.6
        range2 = target1 * 0.8
        rangex = max(revenue1, target1) * 1.1

        fig.add_trace(go.Indicator(
            mode="number+gauge+delta",
            value=revenue1,
            delta={'reference': revenue1},
            domain={'x': [0.25, 1], 'y': [0.7, 0.9]},
            title={'text': "2018 Revenue ($CAD)"},
            gauge={
                'shape': "bullet",
                'axis': {'range': [None, rangex]},
                'threshold': {
                    'line': {'color': "black", 'width': 2},
                    'thickness': 0.75,
                    'value': target1},
                'steps': [
                    {'range': [0, range1], 'color': "gray"},
                    {'range': [range1, range2], 'color': "lightgray"}],
                'bar': {'color': "black"}}))
        fig.update_layout(margin={'t': 0, 'b': 0, 'l': 0})

        pyo.write_html(fig, file='RevenueVsRevenue.html', auto_open=False)
