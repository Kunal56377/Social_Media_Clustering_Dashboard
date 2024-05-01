from dash import Dash,html, dcc 
import plotly.express as px
import pandas as pd

app = Dash('Cluster Dashboard')

# Load data using pandas

df = pd.read_csv("cluster_data.csv")

fig1 = px.scatter(df, x ='num_comments',y = 'num_reactions',color='cluster')
fig2 = px.scatter(df, x ='num_shares',y = 'num_likes',color='cluster')
fig3 = px.scatter(df, x ='num_hahas',y = 'num_sads',color='cluster')
fig4 = px.scatter(df, x ='num_loves',y = 'num_wows',color='cluster')

app.layout = html.Div(
  children= [
    html.H1(children='Cluster Dashboard'),
    html.Div(children = "Showcasing your results using Dash"),
    html.Div(children=[
      html.Div(dcc.Graph(id='comments',figure=fig1),style={'display':'inline-block'}),
      html.Div(dcc.Graph(id='shares',figure=fig2),style={'display':'inline-block'})
    ]),
    html.Div(children=[
      html.Div(dcc.Graph(id='hahas',figure=fig3),style={'display':'inline-block'}),
      html.Div(dcc.Graph(id='loves',figure=fig4),style={'display':'inline-block'})
    ])
  ],
  style={'font-family':'Roboto', 'margin' : '0 auto', 'width' : '1400px'}
)

# Run the application
if __name__ == '__main__':
  app.run_server(debug=True)


