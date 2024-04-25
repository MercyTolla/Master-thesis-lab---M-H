import pandas as pd 
import plotly.graph_objects as go
import numpy as np

#Les output data fra testene
#Test 1. Etanol - 2.Vann - 3. WBM - 4.OBM
def read_file(filename):
    df = pd.read_excel(filename)
    
    #for column in df.columns:
    #    df[column] = df[column].apply(lambda x: str(x).replace(',', '.'))
    
    df.set_index('Time  1 - default sample rate [s]', inplace=True)
    columns = df.columns
    
    #Parametere: (Hva skal vi se på?)
    flow = df["Flow meter [l/min]"]
    df["Inlet cell [kg]"] = df["Inlet cell [kg]"].astype(str).astype(int) #Vekt inlet cell [g]
    df["Outlet cell [kg]"] = df["Outlet cell [kg]"].astype(str).astype(int) #Vekt outlet cell [g]

    fig = go.Figure()

    # Trace for flow velocity
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Flow meter [l/min]'],
            mode='lines',
            name='Velocity [l/min]',
            line=dict(color='purple', width=1),
            yaxis='y2'
        )
    )
    
    # Trace for cell1
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Inlet cell [kg]'],
            mode='lines',
            name='Inlet cell [kg]',
            line=dict(color='blue', width=1),
            yaxis='y'
        )
    )

    # Trace for cell2
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df['Outlet cell [kg]'],
            mode='lines',
            name='Outlet cell [kg]',
            line=dict(color='green', width=1),
            yaxis='y'
        )
    )
    
    # Update layout
    fig.update_layout(
        title='Time vs Velocity',
        xaxis_title='Time [s]',
        yaxis_title='Weight [kg]',
        yaxis=dict(title='Weight [kg]', overlaying='y', side='left'),  # Primary y-axis
        yaxis2=dict(title='Velocity [l/min]', overlaying='y', side='right'),  # Secondary y-axis
        legend=dict(x=0, y=1),
        height=800,
        xaxis=dict(range=[0, 1000])
    )

    
    # Set tick values for x and y axes
    x_tickvals = [0, 100, 200, 300, 400, 500, 600, 700]
    x_ticktext = [str(val) for val in x_tickvals]
    #y_tickvals = [0, 50, 100, 150, 200]
    #y_ticktext = [str(val) for val in y_tickvals]
    fig.update_xaxes(tickvals=x_tickvals, ticktext=x_ticktext)
    #fig.update_yaxes(tickvals=y_tickvals, ticktext=y_ticktext)

    # Show the plot
    fig.show()
    print(df.head())
    print(df.dtypes)


print(read_file("Data/water_test5.xlsm"))



#Modellering, regresjon etc? 