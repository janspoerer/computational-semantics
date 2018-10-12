def test(x):
    x = [1, 2, 3]

i = [4, 5, 6]
test(i)
print(i)

def test(x):
    x[0] = 1
    x[1] = 2
    x[2] = 3

i = [4, 5, 6]
test(i)
print(i)
