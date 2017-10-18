from django.shortcuts import render
from django.views.generic import TemplateView


import plotly.offline as opy
import plotly.graph_objs as go
import math
import numpy as np

from .forms import CoeffForm

# Create your views here.
def index(request):
    # step1 = ''
    form1 = CoeffForm()
    return render(request, 'index.html', {'form1' : form1})

def result(request):

    t_s = float(request.GET.get('surrounding_temperature'))
    t_0 = float(request.GET.get('init_temperature'))
    t_f = float(request.GET.get('final_temperature'))
    s = float(request.GET.get('time_elapsed'))
    k = 0.0

    k = (-1.0/s) * math.log(((t_f-t_s)/(t_0-t_s)))

    time_array = np.linspace(0.0, s, num=10)

    print(time_array)

    temp_array = []

    def temp_func(time_array): 
        for s in time_array:
            t_f = t_s + (t_0 - t_s) * math.exp(-(k)*s)
            temp_array.append(t_f)

    temp_func(time_array)

    print(temp_array)

    # Create traces
    trace0 = go.Scatter(
        x = time_array,
        y = temp_array,
        mode = 'lines+markers',
        line=dict(color='00CED1', width=2),
        name = 'lines',
        error_y=dict(
        type='data',
        # array=[5, 5, 5],
        visible=True
        )
    )

    data = [trace0]

    div = opy.plot(data, auto_open=False, output_type='div', show_link=False)

    return render(request, 'results.html', {'graph': div, 'constant': k, 'surrounding_temperature' : t_s, 'initial_temp' : t_0, 'final_temperature': t_f, 'time_elapsed': s})


def graph(request):

        time_array = np.linspace(0.0, 1200.0, num=10)

        temp_array = [373.000000, 358.498460, 346.625604, 336.904931, 328.946317, 322.430355, 317.095537, 312.727757, 309.151721, 306.223911]

        # Create traces
        trace0 = go.Scatter(
            x = time_array,
            y = temp_array,
            mode = 'lines+markers',
            line=dict(color='00CED1', width=2),
            name = 'lines',
            error_y=dict(
            type='data',
            array=[5, 5, 5],
            visible=True
            )
        )


        data = [trace0]

        div = opy.plot(data, auto_open=False, output_type='div', show_link=False)

        return render(request, 'graph.html', {'graph': div})

# class graph(TemplateView):
#     template_name = 'graph.html'

#     def get_context_data(self, **kwargs):
#         context = super(graph, self).get_context_data(**kwargs)

#         N = 100
#         random_x = np.linspace(0, 1, N)
#         random_y0 = np.random.randn(N)+5
#         random_y1 = np.random.randn(N)
#         random_y2 = np.random.randn(N)-5

#         # Create traces
#         trace0 = go.Scatter(
#             x = random_x,
#             y = random_y0,
#             mode = 'lines',
#             name = 'lines'
#         )


#         data = [trace0]

#         div = opy.plot(data, auto_open=False, output_type='div', show_link=False)

#         # context = super(graph, self).get_context_data(**kwargs)

#         # x = [-2,0,4,6,7]
#         # y = [q**2-q+3 for q in x]
#         # trace1 = go.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
#         #                     mode="lines",  name='1st Trace')

#         # data=go.Data([trace1])
#         # layout=go.Layout(title="Meine Daten", xaxis={'title':'x1'}, yaxis={'title':'x2'})
#         # figure=go.Figure(data=data,layout=layout)
#         # div = opy.plot(figure, auto_open=False, output_type='div')

#         context['graph'] = div

#         return context