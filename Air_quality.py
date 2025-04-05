import matplotlib.pyplot as plt
import pandas as pd

 # put Air Quality Data into Dataframe
df = pd.read_csv('Air_Quality.csv')

 # Remove and filter columns and rows that we are not using for this analysis, also convert Start_Date to a datetime
cols = df[["Unique ID", "Name", 'Measure',"Measure Info", "Geo Place Name", "Start_Date", "Data Value"]]
PM_df = cols[cols["Name"] == "Fine particles (PM 2.5)"]
PM_df.loc[:,"Start_Date"] = pd.to_datetime(PM_df['Start_Date'])
 # test 1 
# print(PM_df.dtypes)
 #test 2
 # Figure out how many unique values in each column
#print("How Many Unique Values are in each column?\n" + str(PM_df.nunique()))
 # There are 114 locations, 39 unique Start_Dates, and only one Measure and Measure Info
PM_df1 = PM_df.drop(["Name", "Measure", "Measure Info"],axis=1)

 ### Part 1. When is the highest amount of PM2.5? At what point is it highest? When is the lowest amount of PM2.5?
 # Group and find max Start Date and Date Value to see highest Data Value at each time
Group_df = PM_df1.groupby(["Start_Date"], as_index=False).agg({"Data Value" : ['mean', 'min', 'max']})
#print(Group_df)
 # Plot this on matplotlib 
plt.plot(Group_df.loc[:,'Start_Date'],Group_df.loc[:,('Data Value', 'mean')])
plt.plot(Group_df.loc[:,'Start_Date'],Group_df.loc[:,('Data Value', 'min')])
plt.plot(Group_df.loc[:,'Start_Date'],Group_df.loc[:,('Data Value', 'max')])
#plt.show()

 # Let's group the things by location
Location_Group_df = PM_df1.groupby(["Geo Place Name"], as_index=False).agg({"Data Value" : ['mean', 'min', 'max']})
#print(Location_Group_df)
 # Print the 10 Locations where max are the greatest
print(Location_Group_df.sort_values(('Data Value', 'max'), ascending=False).head(10)) 
 # Check how different the locations are if we check which mean is the max
print(Location_Group_df.sort_values(('Data Value', 'mean'), ascending=False).head(10)) 

# plotting
#plt.scatter("Start_Date", "Data Value", data=PM_df1)
#plt.xlabel("Date")
#plt.ylabel("Mean PM2.5 Levels in ppb")
#plt.show()

### 