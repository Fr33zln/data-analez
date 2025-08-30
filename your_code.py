import pandas as pd

# Завантажуємо датафрейм 
df = pd.read_csv('GoogleApps.csv')

#df.info()
#print(df.head(2))
#print(df.tail(2))
#print(df.describe())
#print(df["Price"].min())
#print(df[df["Rating"]>4.9])
#print(df[df["Rating"]>4.9]["Installs"])
#print(df[df["Rating"]>4.9]["Installs"].mean())
#
#print(df[(df["Rating"]>4.9)&(df["Type"] =="Free")]["Installs"].max())
#
#
#print(df["Reviews"]&(df["Type"] =="Free")["Price"].max())
#print(df["Reviews"]&(df["Type"] =="Paid")["Price"].max())

print(df[(df["Rating"]>4.9)&(df["Type"] =="Paid")]["Installs"].max())
print(df[(df["Rating"]>4.9)&(df["Type"] =="Free")]["Reviews"].max())