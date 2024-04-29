import pandas as pd 
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def read_file(filename):
    df = pd.read_excel(filename)
    
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).replace(',', '.'))
        df[column] = pd.to_numeric(df[column], errors='coerce')

    df.set_index('Time  1 - default sample rate [s]', inplace=True)
    
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add traces
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Flow meter [l/min]'],
            mode='lines',
            name='Velocity [l/min]',
            line=dict(color='purple', width=2),
        ),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Inlet cell [kg]'],
            mode='lines',
            name='Inlet cell [kg]',
            line=dict(color='blue', width=1.5),
        ),
        secondary_y=True,
    )

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Outlet cell [kg]'],
            mode='lines',
            name='Outlet cell [kg]',
            line=dict(color='green', width=1.5),
        ),
        secondary_y=True,
    )
    
    # Update layout
    fig.update_layout(
        title='Time vs Weight, Velocity',
        xaxis_title='Time [s]',
        legend=dict(x=0, y=1),
        height=800,
    )
    
    fig.update_yaxes(title_text="Velocity [l/min]", secondary_y=False)
    fig.update_yaxes(title_text="Weight [kg]", secondary_y=True)

    #x_tickvals = [0, 100, 200, 300, 400]
    #x_ticktext = [str(val) for val in x_tickvals]
    #fig.update_xaxes(tickvals=x_tickvals, ticktext=x_ticktext)

    # Show the plot
    fig.show()
    #print(df.head())
    #print(df.dtypes)


read_file("Data/obm_test3.xlsm")