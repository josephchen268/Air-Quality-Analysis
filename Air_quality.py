import pandas as pd

# put Air Quality Data into Dataframe
df = pd.read_csv('Air_Quality.csv')

# Remove and filter columns and rows that we are not using for this analysis
cols = df[["Unique ID", "Name", 'Measure',"Measure Info", "Geo Place Name", "Start_Date", "Data Value"]]
PM_df = cols[cols["Name"] == "Fine particles (PM 2.5)"]
print(PM_df.head())