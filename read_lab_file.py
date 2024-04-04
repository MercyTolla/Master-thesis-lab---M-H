import pandas as pd 

#Les output data fra testene
#Test 1. Etanol - 2.Vann - 3. WBM - 4.OBM
def read_file(filename):
    df = pd.read_csv(filename, delimiter='\t', parse_dates=True, index_col='Time')
    df["Time"] = df.index
    columns = df.columns

    #for column in columns:
    #    df[column] = df[column].str.replace(',', '.').astype(float) #Bare nødvendig om filen bruker komma som seperator og ikke punktum
        
    df.set_index("Time", inplace = True)
    return df

#Parametere: (Hva skal vi se på?)
flow = df["Flowrate"]
cell1 = df[] #Vekt inlet cell [g]
cell2 = df[] #Vekt outlet cell [g]




#Skal vi plotte noe? 




#Modellering, regresjon etc? 