print('--Transformando °C em °F --')

import random
celsius = []
fahren = []
i = 0

for i in range(0,5):
    celsius.append(random.randrange(-14, 46))
print('As temperaturas em °Celsius:\n', celsius)

for i in range (0,5):
    fahren.append(celsius[i] * 9/5 + 32)
print('As temperaturas em °Fahrenheit:\n', fahren)
