import random
import time
import matplotlib.pyplot as plt

results = []
decksizes = [10, 100, 1000, 2000, 3000]
repetition_limit = 10

def sort_list( state, ascending = True ):
    j = 1
    for j in range( j, len(state) ):
        key = state[j]
        i = j - 1
        if ascending:
            while i >= 0 and state[i] > key:
                state[i + 1] = state[i]
                i = i - 1
        else:
            while i >= 0 and state[i] < key:
                state[i + 1] = state[i]
                i = i - 1
        state[i + 1] = key

def track_time_complexity( decksizes, repetition_limit ):
    for n in range(0, len( decksizes )):
        sum = 0
        for repetition in range( 1, repetition_limit ):
            state = list( reversed( range( decksizes[n] ) ) )

            start = time.time()
            sort_list( state )
            sum = sum + ( time.time() - start )
        average = sum / repetition_limit
        print( sum )
        results.append ( average )
    return results

results = track_time_complexity( decksizes, repetition_limit )

plt.plot( results )
plt.ylabel( 'time complexity' )
plt.show()
