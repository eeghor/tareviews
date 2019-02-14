import os
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

server = app.server

df = pd.read_csv('reviews.csv')

def selector(dk):

    """
    dk is {'column': value}
    """
    
    if not (set(dk) <= set(df.columns)):
        print('wrong segments!')
        raise Exception()
        
    out = t.data
    
    for k in dk:
        out = out[out[k] == dk[k]]
        
    if not out.empty:
        return out
    else:
        print('empty result!')
        raise Exception()

female_lux_df = selector({'gender': 'f', 'luxury traveller': 1})
male_foodie_df = selector({'gender': 'm', 'foodie': 1})

d1 = female_lux_df[['date_of_experience', 'id']].groupby(['date_of_experience']).count().reset_index()
d1['date_of_experience'] = d1['date_of_experience'].apply(lambda x: arrow.get(x, 'MM/YYYY'))
d2 = male_foodie_df[['date_of_experience', 'id']].groupby(['date_of_experience']).count().reset_index()
d2['date_of_experience'] = d2['date_of_experience'].apply(lambda x: arrow.get(x, 'MM/YYYY'))

d1_scatter = go.Scatter(x=d1.date_of_experience, 
                            y=d1.id, mode='markers', 
                               marker=dict(size=12, line=dict(width=0),color="orange"),
                                name='Luxury Females', text='pidgeons diamonds ticket cruise nice',)

d2_scatter = go.Scatter(x=d2.date_of_experience, 
                            y=d2.id, mode='markers', 
                               marker=dict(size=12, line=dict(width=0),color="#2C72EC"),
                                name='Foodie Males', text='pizza expensive rip-off sucks chips',)

fig_data = [d1_scatter, d2_scatter]

layout_both = go.Layout(
                title='Reviews for Sydney Opera House',
                hovermode='closest',
                    xaxis=dict(title='date', ticklen=5, zeroline=False, gridwidth=2),
                    yaxis=dict(title='# reviews', ticklen=5, gridwidth=2),
                    )

fig = go.Figure(data=fig_data, layout=layout_both)


app.layout = html.Div([
    dcc.Graph(
        id='opera-house-reviews',
        figure={
            'data': [d1_scatter, d2_scatter],
            'layout': go.Layout(
                xaxis={'title': 'Date'},
                yaxis={'title': 'Number of Reviews'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)