import pandas as pd

# put Air Quality Data into Dataframe
df = pd.read_csv('Air_Quality.csv')

# Remove and filter columns and rows that we are not using for this analysis
cols = df[["Unique ID", "Name", 'Measure',"Measure Info", "Geo Place Name", "Start_Date", "Data Value"]]
PM_df = cols[cols["Name"] == "Fine particles (PM 2.5)"]
#print(PM_df.head())

# Figure out how many unique values in each column
print("How Many Unique Values are in each column?\n" + str(PM_df.nunique()))
# There are 114 locations, 39 unique Start_Dates, and only one Measure and Measure Info
PM_df1 = PM_df.drop(["Name", "Measure", "Measure Info"],axis=1)

### Part 1. Where is the highest amount of PM2.5? At what point is it highest? Where is the lowest amount of PM2.5?
# Group and find max Start Date and Date Value to see highest Data Value at each time
Group_df = PM_df1.groupby(["Start_Date"]).max()
#print(Group_df)
## At every time, from 01/01/2015 - 01/01/2020, the place with the most Fine particles is Woodside and Sunnyside (CD2)

# Let's group the things by location
Loc_Group_df = PM_df1.groupby(["Geo Place Name"]).max()
print("Listed Unique Start Date Values for the max PM2.5 values \n" + str(Loc_Group_df["Start_Date"].unique()))
# Since it checks unique values, it seems that the for every location, the highest concentration of PM2.5 is at time 12/31/2015.
# This suggests that the highest concentration of PM2.5 is at 12/31/2015. It also means that the PM2.5 concentration 
print(PM_df["Start_Date"].unique())

###