import pandas as pd

def read_file(filename):
    df = pd.read_excel(filename)
    
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).replace(',', '.'))
    
    df.set_index('Time  1 - default sample rate [s]', inplace=True)
    columns = df.columns

    return df

#Calculate Reynolds number
def Re(rho_m, avg_v, mu):
    d = 0.15  # m
    Re = rho_m * avg_v * d / mu
    return Re

#Test 1 water 
df_w = read_file("water_test3.xlsm")
rho_w = 1000  #kg/m^3
mu_w = 1.002 * 10**(-3)  #Pa*s

# Convert "Flow meter [l/min]" column to numeric values
avg_vw = pd.to_numeric(df_w["Flow meter [l/min]"], errors='coerce')  # Convert to numeric, handling errors

# Filter out any NaN values
avg_vw = avg_vw.dropna()

reynolds_numbers = Re(rho_w, avg_vw, mu_w)
print(reynolds_numbers)