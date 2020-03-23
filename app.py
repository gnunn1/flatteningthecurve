from flask import Flask, render_template
import requests
import plotly.graph_objects as go

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get("https://ihs-api.herokuapp.com/covid/allc")
    data = r.json()
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=list(data["Italy"].keys()), y=list(data["Italy"].values()),
                    mode='lines',
                    name='Italy', line=dict(color='#BF55EC', width=6)))
    fig.add_trace(go.Scatter(x=list(data["Ontario"].keys()), y=list(data["Ontario"].values()),
                    mode='lines+markers',
                    name='Ontario',line=dict(color='#F1F227', width=6), marker=dict(size=15)))
    fig.add_trace(go.Scatter(x=list(data["Singapore"].keys()), y=list(data["Singapore"].values()),
                    mode='lines',
                    name='Singapore',line=dict(color='#32CD32', width=6)))
    fig.add_trace(go.Scatter(x=list(data["South Korea"].keys()), y=list(data["South Korea"].values()),
                    mode='lines',
                    name='South Korea', line=dict(color='#00CED1', width=6)))
    fig.update_layout(
                    autosize=True,
                    width=1200,
                    height=1000,
                   xaxis_title='Days after 100 confirmed cases',
                   yaxis_title='ICU beds',
                   yaxis_range=[0,500],plot_bgcolor="#333333")
    fig.add_shape(
        # Line Horizontal
            type="line",
            x0=0,
            y0=375,
            x1=30,
            y1=375,
            name="1",
            line=dict(
                color="#FFFFFF",
                width=5,
                dash="dashdot",
            ),
    )

    fig.add_shape(
        # Line Horizontal
            type="line",
            x0=0,
            y0=170,
            x1=30,
            y1=170,
            line=dict(
                color="#FFFFFF",
                width=5,
                dash="dash",
            ),
    )

    fig.add_trace(go.Scatter(
    x=[3, 3],
    y=[175, 380],
    text=["10% ICU Capacity",
          "25% ICU Capacity"],
    mode="text",
    showlegend=False,
    textfont=dict(
        family="sans serif",
        size=12,
        color="#FFFFFF"
    )
        ))
    div = fig.to_html(full_html=True)
    return render_template('index.html', plot=div)

@app.route('/about')
def about():
    return render_template('story.html')
