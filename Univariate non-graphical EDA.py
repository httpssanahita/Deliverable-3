    #Teammates: Anahita N. , Jasmine B. amd Ruby F.

import pandas as pd

data= pd.read_csv ("air_quality_health_dataset.csv")

# Summary function of each numerical variabes 

#1) AQI

aqi_mean= data["aqi"].mean()
print(aqi_mean) # Mean = 249.3701816044932

aqi_median= data["aqi"].median()
print(aqi_median) # Median= 249.0


aqi_mode= data["aqi"].mode()
print(aqi_mode) #10 


aqi_std= data["aqi"].std()
print(aqi_std) #144.47913170506766

aqi_variance= data["aqi"].var()
print(aqi_variance) #20874.219498250284


aqi_skew= data["aqi"].skew()
print(aqi_skew) #0.0008269989044437379


aqi_kurtosis = data["aqi"].kurt()
print(aqi_kurtosis ) #-1.1976435540188488


aqi_quartiles = data["aqi"].quantile([0.25, 0.5, 0.75])
print(aqi_quartiles) #124.0 , 249.0 and 374.0

#2) pm2_5
pm2_5_mean= data["pm2_5"].mean()
print(pm2_5_mean) 

pm2_5_median= data["pm2_5"].median()
print(pm2_5_median) 


pm2_5_mode= data["pm2_5"].mode()
print(pm2_5_mode) 


pm2_5_std= data["pm2_5"].std()
print(pm2_5_std) 

pm2_5_variance= data["pm2_5"].var()
print(pm2_5_variance) 


pm2_5_skew= data["pm2_5"].skew()
print(pm2_5_skew)


aqi_kurtosis = data["pm2_5"].kurt()
print(aqi_kurtosis )


pm2_5_quartiles = data["pm2_5"].quantile([0.25, 0.5, 0.75])
print(pm2_5_quartiles) 




#3) pm10
#4) no2
#5) o3
#6) temperature 
#7) humidity
#8) hospital_admissions
#9) hospital_capacity


# Manipulating categorical variables

# City

city_frequency= data["city"].value_counts()
print(city_frequency)

city_proportion= data["city"].value_counts(normalize=True)
print(city_proportion)

city_mode= data["city"].mode()
print(city_mode) # Delhi

city_unique= data["city"].nunique()
print(city_unique) 



# population_density
population_density_frequency= data["population_density"].value_counts()
print(population_density_frequency)

population_density_proportion= data["population_density"].value_counts(normalize=True)
print(population_density_proportion)

population_density_mode= data["population_density"].mode()
print(population_density_mode) 

population_density_unique= data["population_density"].nunique()
print(population_density_unique) 

