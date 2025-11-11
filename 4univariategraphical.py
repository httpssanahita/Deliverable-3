import pandas as pd
import seaborn as sns

data= pd.read_csv ("air_quality_health_dataset.csv")

numerical_data= data[['aqi', "pm2_5", "pm10", "no2", "o3", "temperature", "humidity", "hospital_admissions", "hospital_capacity"]]
#Create a visualization
#a)
for i in numerical_data:
    sns.displot(data, x=i, bins=10)
#b-c)Conditioning on other variables & Stacked Histogram
    sns.displot(data, x=i, hue="population_density", bins=10)
#d)Dodge Bars
    sns.displot(data, x=i, hue="population_density", multiple="dodge", bins=10)
#e)Normalized Histogram Statistics
    sns.displot(data, x=i, hue="population_density", stat="density", common_norm=False)
#f)Kernel Density Estimation
    sns.displot(data, x=i, kind="kde", bw_adjust=1.5)
#gEmpirical Cumulative Distributions
    sns.displot(data, x=i, hue="city", kind="ecdf")