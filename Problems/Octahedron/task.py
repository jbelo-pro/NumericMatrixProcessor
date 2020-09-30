import math
edge = float(input())

area = 2 * math.sqrt(3) * edge ** 2
volume = (math.sqrt(2) * edge ** 3) / 3

print(round(area, 2), round(volume, 2))