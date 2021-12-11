import os, sys
import pandas as pd
import plotly.express as px


df = pd.read_csv(str(sys.argv[1])+'.csv')
fig = px.violin(df, x="<b>Sequence</b>", y="<b>Score</b>", color="<b>Sequence</b>", box=True,title="<b>Violin plot depicting score distribution on ten different sequence</b>")
fig.show()
