import pandas as pd
import plotly.graph_objects as go

def read_file(filename):
    df = pd.read_excel(filename)
    
    for column in df.columns:
        df[column] = df[column].apply(lambda x: str(x).replace(',', '.'))
    
    df.set_index('Time  1 - default sample rate [s]', inplace=True)

    return df

# Calculate Reynolds number
def Re(rho_m, avg_v, mu):
    d = 0.15  # m
    avg_v_m_s = avg_v / 600.0  # Convert l/min to m/s
    return rho_m * avg_v_m_s * d / mu

# Prepare data
data = {
    "Water": [
        ("Data/water_test3.xlsm", "Test 1 Water"),
        ("Data/water_test4.xlsm", "Test 2 Water"),
        ("Data/water_test6(2).xlsm", "Test 3 Water")
    ],
    "OBM-1": [
        ("Data/obm_test1.xlsm", "Test 1 OBM-1"),
        ("Data/obm_test2.xlsm", "Test 2 OBM-1"),
        ("Data/obm_test4(3).xlsm", "Test 3 OBM-1")
    ]
}

# Plot
fig = go.Figure()

for fluid, tests in data.items():
    for test_data in tests:
        df = read_file(test_data[0])
        avg_v = pd.to_numeric(df["Flow meter [l/min]"], errors='coerce').dropna()
        reynolds = round(Re(1000 if fluid == "Water" else 2100, avg_v, 1.002 * 10**(-3) if fluid == "Water" else 4.305 * 10**(-2)))
        fig.add_trace(go.Scatter(x=df.index, y=[reynolds]*len(df.index), mode='markers+lines', name=test_data[1]))

fig.update_layout(
    title='Reynolds Number for Different Tests',
    xaxis_title='Time [s]',
    yaxis_title='Reynolds Number',
    legend=dict(x=0, y=1),
)

fig.show()