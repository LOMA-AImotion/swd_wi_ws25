sensor = [3.2, 10.0, 2.8, 4.5, 6.4, -3.2, 2.9, 5.6, -1.2]

reversed_sensor = sensor[::-1]
print(reversed_sensor)

half_index = (len(sensor) + 1) // 2

subsampled_sensor = sensor[:half_index:2]

print(subsampled_sensor)