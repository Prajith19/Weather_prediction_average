import requests
response = requests.get("https://archive-api.open-meteo.com/v1/archive?latitude=13.02&longitude=80.27&start_date=2000-01-01&end_date=2023-01-01&daily=weathercode,apparent_temperature_min,apparent_temperature_max,precipitation_sum,windspeed_10m_max&timezone=auto")
data = response.json()


import pandas as pd
df = pd.DataFrame.from_dict(data)



newdf = df['daily']


weathercode = []
apparent_temperature_max = []
apparent_temperature_min = []
precipitation_sum = []
windspeed_10m_max = []


def singletwo(number):
  if(len(str(number)) == 1):
    return "0"+str(number)
  return str(number)


date = int(input("Enter the Date : "))
month = int(input("Enter the month : "))
year = int(input("Enter the year :"))


for i in range(23):
  ydm = "20"+singletwo(i)+"-"+singletwo(month)+"-"+singletwo(date)
  seldate = newdf['time'].index(ydm)
  weathercode.append(newdf['weathercode'][seldate])
  apparent_temperature_max.append(newdf['apparent_temperature_max'][seldate])
  apparent_temperature_min.append(newdf['apparent_temperature_min'][seldate])
  precipitation_sum.append(newdf['precipitation_sum'][seldate])
  windspeed_10m_max.append(newdf['windspeed_10m_max'][seldate])


print("                     ")
print(f'Weather_code {weathercode}')
print("                     ")
print(f'Apparent_temperature_max {apparent_temperature_max}')
print("                     ")
print(f'Apparent_temperature_min {apparent_temperature_min}')
print("                     ")
print(f'Precipitation_sum {precipitation_sum}')
print("                     ")
print(f'Windspeed_10_max {windspeed_10m_max}')

predicted_weather_code = max(set(weathercode),key=weathercode.count)
predicted_apparent_temperature_max = sum(apparent_temperature_max)/len(apparent_temperature_max)
predicted_apparent_temperature_min = sum(apparent_temperature_min)/len(apparent_temperature_min)
predicted_precipitation_sum = sum(precipitation_sum)/len(precipitation_sum)
predicted_windspeed_10_max = sum(windspeed_10m_max)/len(windspeed_10m_max)

round_weather_code = round(predicted_weather_code,0)
round_apparent_temperature_max = round(predicted_apparent_temperature_max,0)
round_apparent_temperature_min = round(predicted_apparent_temperature_min,0)
round_precipitation_sum = round(predicted_precipitation_sum,0)
round_windspeed_10_max = round(predicted_windspeed_10_max,0)


print("                     ")
print(f'Predicted weather for {date}/{month}/{year} is')
print(f'Predicted Weathercode --> {round_weather_code}')
print(f'Predicted apparent_temperature_max --> {round_apparent_temperature_max} °C')
print(f'Predicted apparent_temperature_min --> {round_apparent_temperature_min} °C')
print(f'Predicted Precipitation Sum --> {round_precipitation_sum} mm')
print(f'Predicted Windspeed_10m_max --> {round_windspeed_10_max} km/h')
print("                      ")
if round_weather_code >= 0 and round_weather_code <= 3:
    print("Description --> Clear sky, no precipitation")

if round_weather_code >=4 and round_weather_code <= 9:
    print("Description --> Haze, dust, sand or smoke")
    
if round_weather_code >=10 and round_weather_code <=19:
    print("Description --> Patches of shallow fog, lightning visible, precipitation within sight, funnel clouds")
    
if round_weather_code >=20 and round_weather_code <=29:
    print("Description --> Precipitation, fog, ice fog or thunderstorm during the preceding hour but not at the time of observation")

if round_weather_code >=30 and round_weather_code <=39:
    print("Description --> Duststorm, sandstorm, drifting or blowing snow")
    
if round_weather_code >=40 and round_weather_code <=49:
    print("Description --> Fog or ice fog at the time of observation")
    
if round_weather_code >=50 and round_weather_code <=59:
    print("Description --> Drizzle")
    
if round_weather_code >=60 and round_weather_code <=69:
    print("Description --> Rain")
    
if round_weather_code >=70 and round_weather_code <=79:
    print("Description --> Solid precipitation not in showers")
    
if round_weather_code >=80 and round_weather_code <=99:
    print("Description --> Showery precipitation, or precipitation with current or recent thunder storm")
