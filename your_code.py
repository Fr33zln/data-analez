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
#
#print(df[(df["Rating"]>4.9)&(df["Type"] =="Paid")]["Installs"].max())
#print(df[(df["Rating"]>4.9)&(df["Type"] =="Free")]["Reviews"].max())

#df.info()
#result = df["Category"].value_counts()["BUSINESS"]
#print(result)
#

#result = df["Content Rating"].value_counts()["Teen"] / df["Content Rating"].value_counts()["Everyone 10+"]
#print(result)
##print(df["Installs"].value_counts())


#b =(round(df[df["Type"] == "Paid"]["Rating"].mean(),2))
#
#a = (round(df[df["Type"] == "Free"]["Rating"].mean(),2))
#
#print(b-a)
#

#print(df[df["Category"] == "COMICS"]["Size"].agg(["max","min"]))


#print(df[(df["Category"] == "FINANCE") & (df["Rating"] > 4.5)])


#a = (df[(df["Type"] == "Free") & (df["Rating"] > 4.9)&(df["Category"] == "GAME")])
#b = (df[(df["Type"] == "Paid") & (df["Rating"] > 4.9)&(df["Category"] == "GAME")])
##print(a/b)
#
#print(a)
#print(b)

print(df.groupby(by = "Type")["Rating"].agg(["min","mean","max"]))