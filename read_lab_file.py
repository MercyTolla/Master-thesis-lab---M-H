import pandas as pd 
import plotly.graph_objects as go
import numpy as np

#Les output data fra testene
#Test 1. Etanol - 2.Vann - 3. WBM - 4.OBM
def read_file(filename):
    df = pd.read_excel(filename)
    
    for column in df.columns:
        df[column] = df[column].replace(',', '.')
    
    df.set_index('Time  1 - default sample rate [s]', inplace=True)
    columns = df.columns
    
    #y_tickvals = [0, 200, 400, 600, 800, 1000, 1500]
    #y_ticktext = [str(val) for val in y_tickvals]

    x_tickvals = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
    x_ticktext = [str(val) for val in x_tickvals]

            
    #Parametere: (Hva skal vi se på?)
    flow = df["Flow meter [l/min]"]
    cell1 = df["Inlet cell [kg]"] #Vekt inlet cell [g]
    cell2 = df["Outlet cell [kg]"] #Vekt outlet cell [g]

    fig = go.Figure()

    #Trace for flow velocity
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=flow,
            #y=df["MX840B_CH 4 [kg]"],
            mode='lines',
            name='Velocity [l/min]',
            line=dict(color='purple', width=1),  
        )
    )
    
    # Trace for cell1
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=cell1,
            mode='lines',
            name='Inlet cell [kg]',
            line=dict(color='blue', width=1),
        )
    )

    # Trace for cell2
    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=cell2,
            mode='lines',
            name='Outlet cell [kg]',
            line=dict(color='green', width=1),
        )
    )
    
    fig.update_xaxes(tickvals=x_tickvals, ticktext=x_ticktext)
    
    # Define the layout for OBM
    fig.update_layout(
        title='Time vs Velocity',
        xaxis_title='Time [s]',
        yaxis_title='Velocity [l/min]',
        height=800,
        legend=dict(
            x=0,
            y=1,
        ),
        xaxis=dict(
            range=[0, 1000]
            
        )
    )

    # Show the plot
    fig.show()
    print(df.head())
    print(df.dtypes)


print(read_file("water_test2.xlsm"))


#Skal vi plotte noe? 




#Modellering, regresjon etc? 