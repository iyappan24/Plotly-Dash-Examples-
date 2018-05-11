import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div([

    html.Div(
    [html.Label('DropDown'),
    dcc.Dropdown(options = [{'label':'New York City','value':'NYC'},
                            {'label':'Chicaog','value':'chi'}], #end of options
                value = 'NYC'
    )] #end of drop down one
    ),#end of div one

    html.Div(
    [html.Label('DropDown2'),
    dcc.Dropdown(options = [{'label':'New York City','value':'NYC'},
                            {'label':'Chicaog','value':'chi'},
                            {'label':'Los Angeles','value':'LA'}], #end of options
                value = 'LA',multi= True
    )] #end of drop down two
    )#end of div2

],style={'columnCount': 2}) # this is SPA design with one whole block of the application


if __name__ == '__main__':

    app.run_server()
