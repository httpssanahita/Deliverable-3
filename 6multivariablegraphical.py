import pandas as pd
import seaborn as sns

data= pd.read_csv ("air_quality_health_dataset.csv")

sns.relplot(data=data.head(1826), x="temperature", y="aqi", col="population_density")