# Objective: Find out if datetime is mutable
import datetime

datetime

def test(x):
    x = datetime.replace(year=3000)

i = datetime.date(2000, 1, 1)
test(i)
print(i)

def test(x):
    x[0] = 1
    x[1] = 2
    x[2] = 3

i = [4, 5, 6]
test(i)
print(i)

# datetime.replace -> Mutable datetime method
