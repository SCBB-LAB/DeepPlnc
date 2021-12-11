import plotly.graph_objects as go
import plotly.express as px
import os, sys
import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("<b>Probability score distribution across position for the selected sequences</b>", "<b>Violin plot depicting score distribution on ten different sequence</b>"))

df = pd.read_csv(str(sys.argv[1])+'.csv')
fig.add_trace(go.Scatter(x=df["Position"], y=df['Score'],
                    mode='lines',
                    name=str(sys.argv[1])),
    row=1, col=1)



fig.add_trace(go.Violin(y=df['Score'], box_visible=True, name=str(sys.argv[1])),row=1, col=2)

fig.show()
