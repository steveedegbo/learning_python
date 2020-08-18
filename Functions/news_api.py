import data

weather_data = data.weather

# # print(weather_data.keys())

# # print(weather_data['list'])


forecast_container = weather_data['list']

# # print(type(forecast_container))
# # print(len(forecast_container))

first_item_in_forecast_container = forecast_container[0]
# # print(first_item_in_forecast_container)
# # print(first_item_in_forecast_container.keys())

# #ATTEMPTING TO ACCESS REQUIRED VALUES FROM FIRST ITEM IN FORECAST LIST

# time = first_item_in_forecast_container['dt_txt']
# temp = first_item_in_forecast_container['main']['temp']
# pressure = first_item_in_forecast_container['main']['pressure']
# wind = first_item_in_forecast_container['wind']['speed']
# clouds = first_item_in_forecast_container['weather']

# cloud_description = clouds[0]['description']

# print(time, temp, wind, pressure, cloud_description)

# #ATTEMPT TO ACCESS FOR ALL 40 FORECASTS IN LIST

# print("Time".center(20), "Temp".center(9), "Temp in C".center(10), "Wind".center(12), "Pressure".center(15), "Cloud_desc".center(17), sep =" | ")

# print('-'*95)

# def kel_celc(kelv_temp):
#     celc_temp = round((kelv_temp - 273.15),2)
#     return celc_temp

# for forecast in forecast_container:
#     time = forecast['dt_txt']
#     print(time)
#     temp = forecast['main']['temp']
#     pressure = forecast['main']['pressure']
#     wind = forecast['wind']['speed']
#     clouds = forecast['weather']
#     cloud_description = clouds[0]['description']
    


#     # print(time, temp, wind, pressure, cloud_description)
#     print(f"{time}".center(20), f"{temp} k".center(9), f"{kel_celc(temp)} c".center(10), f"{wind} km/hr".center(12), f"{pressure} mbar".center(15), f"{cloud_description}".center(17), sep =" | ")


# # # Time Temperature Wind Pressure Cloud


# SOLVING WITH FUNCTIONS

def weather():
    for forecast in forecast_container:
        time = forecast['dt_txt']
        temperature = forecast['main']['temp']
        wind = forecast['wind']['speed']
        pressure = forecast['main']['pressure']
        clouds = forecast['weather']
        cloud_description = clouds[0]['description']
        print(time,temperature,wind,pressure,cloud_description)

weather()

