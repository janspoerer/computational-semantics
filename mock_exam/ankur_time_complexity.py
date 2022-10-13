import time
def palindrome_(a):
    if a==a[::-1]:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

multiplicator = 1000000
index = 1
while index <= 4:
 
    drome=["alia"*multiplicator*index,"chuhc"*multiplicator*index,"kuch"*multiplicator*index,"lul"*multiplicator*index,"lol"*multiplicator*index]
    index += 1
    
    time_begin=time.time()
    list(map(palindrome_,drome))
    time_end=time.time()
    resultant_time=time_end-time_begin

print("time taken for best case is",resultant_time*1000000,"microsecond")