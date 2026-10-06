import pandas as pd

df=pd.read_csv("C:\HR_analytics\data\HR_Analytics_cleaned.csv")

df= df.loc[:,~df.columns.str.contains('^Unnamed')]

df.to_csv("C:\HR_analytics\data\pyCLeaned_data.csv",index=False)

print("Done! Your clean file is ready for SQlite.")