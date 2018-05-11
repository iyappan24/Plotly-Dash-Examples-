import dash
import dash_core_components as dcc
import dash_html_components as html

#creating a flask app
app = dash.Dash()

colors = {'background':'#11111'}

app.layout = html.Div(children = [
html.H2("Web Dashboard with Python"),
dcc.Graph(id="bar1",
        figure = {'data':[{'x':[1,2,3,4],'y':[23,24,8,33],'type':'bar','name':'KOBE'},
        {'x':[1,2,3,4],'y':[23,6,11,23],'type':'bar','name':'LEBRON'}
        ],'layout':{
        'title':'BAR PLOTS'
        }
        } #end of figure
    ), #graph function
dcc.Graph(id ="scatter1",
figure = {'data':}
)
])#end of children list #divison

if __name__ == '__main__':
    app.run_server()
