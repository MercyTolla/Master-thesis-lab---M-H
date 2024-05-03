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

#WATER
rho_w = 1000  #kg/m^3
mu_w = 1.002 * 10**(-3)  #Pa*s
#Test 1 water 
df_w1 = read_file("Data/water_test3.xlsm")
avg_vw1 = pd.to_numeric(df_w1["Flow meter [l/min]"], errors='coerce')  # Convert to numeric, handling errors
avg_vw1 = avg_vw1.dropna() #Filter out any NaN values
#print("Test 1", round(Re(rho_w, avg_vw1, mu_w))) 

df_w2 = read_file("Data/water_test4.xlsm")
df_w3 = read_file("Data/water_test6(2).xlsm")


#At time of erosion:
#Test 1 water
#print(round(Re(rho_w, 77.07, mu_w)))
#Test 2 water 
#print(round(Re(rho_w, 72.54, mu_w)))

#---

#OBM-1
rho_o = 2100  #kg/m^3 
mu_o = 4.305 * 10**(-2)  #Pa*s 
#Test 1 oil 
df_o1 = read_file("Data/obm_test1.xlsm")
avg_vo1 = pd.to_numeric(df_o1["Flow meter [l/min]"], errors='coerce')  # Convert to numeric, handling errors
avg_vo1 = avg_vo1.dropna() #Filter out any NaN values
print("Test 1", round(Re(rho_w, avg_vo1, mu_w))) 
#Test 2 oil 
df_o2 = read_file("Data/obm_test2.xlsm")
avg_vo2 = pd.to_numeric(df_o2["Flow meter [l/min]"], errors='coerce')  # Convert to numeric, handling errors
avg_vo2 = avg_vo2.dropna() #Filter out any NaN values
print("Test 2", round(Re(rho_w, avg_vo2, mu_w))) 
#Test 3 oil 
df_o3 = read_file("Data/obm_test4(3).xlsm")
avg_vo3 = pd.to_numeric(df_o3["Flow meter [l/min]"], errors='coerce')  # Convert to numeric, handling errors
avg_vo3 = avg_vo3.dropna() #Filter out any NaN values
print("Test 3", round(Re(rho_w, avg_vo3, mu_w))) 

#At time of erosion:
#Test 1 OBM-1
#print(round(Re(rho_o, 153.45, mu_o)))
#Test 2 OBM-1
#print(round(Re(rho_o, 142.12, mu_o)))

#---

#OBM-2
#...







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
 
