    #Teammates: Anahita N. , Jasmine B. amd Ruby F.
    # description: Univariate non-graphical EDA
    
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


pm2_5_kurtosis = data["pm2_5"].kurt()
print(pm2_5_kurtosis )


pm2_5_quartiles = data["pm2_5"].quantile([0.25, 0.5, 0.75])
print(pm2_5_quartiles) 


#3) pm10
pm10_mean= data["pm10"].mean()
print(pm10_mean) 

pm10_median= data["pm10"].median()
print(pm10_median) 


pm10_mode= data['pm10'].mode()
print(pm10_mode) 


pm10_std= data["pm10"].std()
print(pm10_std) 

pm10_variance= data["pm10"].var()
print(pm10_variance) 


pm10_skew= data["pm10"].skew()
print(pm10_skew)


pm10_kurtosis = data["pm10"].kurt()
print(pm10_kurtosis )


pm10_quartiles = data["pm10"].quantile([0.25, 0.5, 0.75])
print(pm10_quartiles) 

#4) no2
no2_mean= data["no2"].mean()
print(no2_mean) 

no2_median= data["no2"].median()
print(no2_median) 


no2_mode= data['no2'].mode()
print(no2_mode) 


no2_std= data["no2"].std()
print(no2_std) 

no2_variance= data["no2"].var()
print(no2_variance) 


no2_skew= data["no2"].skew()
print(no2_skew)


no2_kurtosis = data["no2"].kurt()
print(no2_kurtosis )


no2_quartiles = data["no2"].quantile([0.25, 0.5, 0.75])
print(no2_quartiles) 

#5) o3
o3_mean= data["o3"].mean()
print(o3_mean) 

o3_median= data["o3"].median()
print(o3_median) 


o3_mode= data['o3'].mode()
print(o3_mode) 


o3_std= data["o3"].std()
print(o3_std) 

o3_variance= data["o3"].var()
print(o3_variance) 


o3_skew= data["o3"].skew()
print(o3_skew)


o3_kurtosis = data["o3"].kurt()
print(o3_kurtosis )


o3_quartiles = data["o3"].quantile([0.25, 0.5, 0.75])
print(o3_quartiles) 

#6) temperature 
temperature_mean= data["temperature"].mean()
print(temperature_mean) 

temperature_median= data["temperature"].median()
print(temperature_median) 


temperature_mode= data['temperature'].mode()
print(temperature_mode) 


temperature_std= data["temperature"].std()
print(temperature_std) 

temperature_variance= data["temperature"].var()
print(temperature_variance) 


temperature_skew= data["temperature"].skew()
print(temperature_skew)


temperature_kurtosis = data["temperature"].kurt()
print(temperature_kurtosis )


temperature_quartiles = data["temperature"].quantile([0.25, 0.5, 0.75])
print(temperature_quartiles)
 
#7) humidity
humidity_mean= data["humidity"].mean()
print(humidity_mean) 

humidity_median= data["humidity"].median()
print(humidity_median) 


humidity_mode= data['humidity'].mode()
print(humidity_mode) 


humidity_std= data["humidity"].std()
print(humidity_std) 

humidity_variance= data["humidity"].var()
print(humidity_variance) 


humidity_skew= data["humidity"].skew()
print(humidity_skew)


humidity_kurtosis = data["humidity"].kurt()
print(humidity_kurtosis )


humidity_quartiles = data["humidity"].quantile([0.25, 0.5, 0.75])
print(humidity_quartiles)


#8) hospital_admissions
hospital_admissions_mean= data["hospital_admissions"].mean()
print(hospital_admissions_mean) 

hospital_admissions_median= data["hospital_admissions"].median()
print(hospital_admissions_median) 


hospital_admissions_mode= data['hospital_admissions'].mode()
print(hospital_admissions_mode) 


hospital_admissions_std= data["hospital_admissions"].std()
print(hospital_admissions_std) 

hospital_admissions_variance= data["hospital_admissions"].var()
print(hospital_admissions_variance) 


hospital_admissions_skew= data["hospital_admissions"].skew()
print(hospital_admissions_skew)


hospital_admissions_kurtosis = data["hospital_admissions"].kurt()
print(hospital_admissions_kurtosis )


hospital_admissions_quartiles = data["hospital_admissions"].quantile([0.25, 0.5, 0.75])
print(hospital_admissions_quartiles)

#9) hospital_capacity
hospital_capacity_mean= data["hospital_capacity"].mean()
print(hospital_capacity_mean) 

hospital_capacity_median= data["hospital_capacity"].median()
print(hospital_capacity_median) 


hospital_capacity_mode= data['hospital_capacity'].mode()
print(hospital_capacity_mode) 


hospital_capacity_std= data["hospital_capacity"].std()
print(hospital_capacity_std) 

hospital_capacity_variance= data["hospital_capacity"].var()
print(hospital_admissions_variance) 


hospital_capacity_skew= data["hospital_capacity"].skew()
print(hospital_capacity_skew)


hospital_capacity_kurtosis = data["hospital_capacity"].kurt()
print(hospital_capacity_kurtosis )


hospital_capacity_quartiles = data["hospital_capacity"].quantile([0.25, 0.5, 0.75])
print(hospital_capacity_quartiles)


# Manipulating categorical variables

# City

city_frequency= data["city"].value_counts()
print(city_frequency)

city_proportion= data["city"].value_counts(normalize=True)
print(city_proportion)

city_mode= data["city"].mode()
print(city_mode) 

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

