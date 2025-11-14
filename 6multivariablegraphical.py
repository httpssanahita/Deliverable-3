import pandas as pd
import seaborn as sns

data= pd.read_csv ("air_quality_health_dataset.csv")

#6.1
#a)
sns.relplot(data=data.head(1826), x="pm2_5", y="hospital_admissions", col="population_density")

#b)
sns.relplot(data=data.head(1826), x="temperature", y="aqi", hue= "humidity", size="city", col="population_density")

#c)
sns.relplot(data=data.head(365), kind="line", x="date", y="o3")

#d)
sns.relplot(data=data.head(365), kind="line", x="date", y="pm10", errorbar="sd")

#e)
sns.lmplot(data=data.head(1826), x="pm2_5", y="hospital_admissions")

#6.2
#a)
sns.catplot(data=data.head(1826), x="population_density", y="aqi")

#b)
sns.catplot(data=data.head(1826), x="population_density", y="pm10", jitter=False)

#c)
sns.catplot(data=data.head(1095), x="population_density", y="pm2_5", kind="swarm", hue="hospital_admissions")

#d)
sns.catplot(data=data.head(1826), x="city", y="o3", kind="box", hue="population_density")

#e)
sns.catplot(data=data.head(1826), x="city", y="temperature", kind="boxen")

#f)
sns.catplot(data=data.head(1826), x="population_density", y="hospital_capacity", kind="violin", col="city", bw_adjust=1.5)

#g)
g = sns.catplot(data=data.head(1826), x="city", y="no2", kind="violin", inner=None)
sns.swarmplot(data=data.head(365), x="city", y="no2", color="k", size=3, ax=g.ax)

#h)
sns.catplot(data=data.head(365), x="city", y="humidity", hue="population_density", errorbar=("pi", 97), kind="bar")

#i) #i don't think this is good
sns.catplot(data=data.head(365), x="city", y="aqi", hue="population_density", errorbar=("pi", 90), linestyles="--", kind="point")

#j)
