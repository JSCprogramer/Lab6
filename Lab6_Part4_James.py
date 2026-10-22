sensor_readings = [23.5, 21,9, 24.0, 26.8, 25.2, 25,6, 21.9, 26.1, 23.7, 26.6, 25,4]
#print("the maximum temperature in the dataset is", max(sensor_readings) ,"degress Celsius")
MAX=0
for i in sensor_readings:
    if i > MAX:
        MAX=i
print(f'The maximum temperature in the dataset is {MAX} degrees Celsius.')
