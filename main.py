import math


def calculatePoints():
    file = open('spiro.kml', 'w')
    file.write('<?xml version="1.0" encoding="UTF-8"?>' + '\n')
    file.write('<kml xmlns="http://earth.google.com/kml/2.0">' + '\n')
    file.write('<Document>' + '\n')
    R = 0.0024
    r = 0.0004
    a = 0.0032
    pi = math.pi
    nRev = 16
    t = 0.0
    while t < nRev * pi:
        x = (R + r) * math.cos((r / R) * t) - a * math.cos((1 + r / R) * t)
        y = (R + r) * math.sin((r / R) * t) - a * math.sin((1 + r / R) * t)
        file.write('<Placemark><Point><coordinates>' + str(-118.2854472 + x) + ',' + str(
            34.0205687 + y) + '</coordinates></Point></Placemark>' + '\n')
        t += 0.01
    file.write('</Document></kml>')


if __name__ == '__main__':
    calculatePoints()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
