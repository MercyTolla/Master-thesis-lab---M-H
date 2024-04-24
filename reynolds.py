import pandas as pd
import plotly.graph_objects as go

def read_file(filename):
    df = pd.read_excel(filename)
    
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).replace(',', '.'))
    
    df.set_index('Time  1 - default sample rate [s]', inplace=True)
    columns = df.columns

    return df

#Calculate Reynolds number
def Re(rho_m, avg_v, mu):
    d = 0.15  #m
    avg_v_m_s = avg_v / 600.0  # Convert l/min to m/s
    Re = rho_m * avg_v_m_s * d / mu
    return Re

#Test 1 water 
df_w1 = read_file("Data/water_test4.xlsm")
df_w2 = read_file("Data/water_test4.xlsm")
rho_w = 1000  #kg/m^3
mu_w = 1.002 * 10**(-3)  #Pa*s

#avg_vw1 = pd.to_numeric(df_w1["Flow meter [l/min]"], errors='coerce')  # Convert to numeric, handling errors
#avg_vw1 = avg_vw.dropna() #Filter out any NaN values
#print(round(Re(rho_w, avg_vw1, mu_w))) 

#At time of erosion - Test 1 water
print(round(Re(rho_w, 77.07, mu_w)))
#Test 2 water 
print(round(Re(rho_w, 72.54, mu_w)))













#Plot (Tviler på at vi trenger dette)

# fig = go.Figure()

# #Trace for flow velocity
# fig.add_trace(
#     go.Scatter(
#         x=df.index,
#         y=flow,
#         mode='lines',
#         name='Velocity [l/min]',
#         line=dict(color='purple', width=1),  
#         )
#     )

# fig.update_layout(
#     title='Time vs Velocity',
#     xaxis_title='Time [s]',
#     yaxis_title='Velocity [l/min]',
#     height=800,
#     legend=dict(
#         x=0,
#         y=1,
#     ),
#     xaxis=dict(
#     range=[0, 1000]
            
#     )
# )

# fig.show()
 
