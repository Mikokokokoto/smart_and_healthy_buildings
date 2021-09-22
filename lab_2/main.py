import pandas as pd
import seaborn as sns

df = pd.read_csv("data.csv")

#3
sns.catplot(x="sesame",kind="count", palette="ch:.25", data=df)
#4
sns.catplot(x="sesame", hue= "sleep", kind="count", palette="ch:.25", data=df)
#5
sns.catplot(x="rps", hue= "sleep", kind="count", palette="ch:.25", data=df)

 