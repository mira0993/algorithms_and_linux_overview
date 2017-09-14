'''
N light bulbs are connected by a wire. Each bulb has a switch associated with it,
however due to faulty wiring, a switch also changes the state of all the bulbs
to the right of current bulb. Given an initial state of all bulbs, find the
minimum number of switches you have to press to turn on all the bulbs.
You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]
'''

def bulbs(A):

    steps = 0
    for bulb in A:
        current_bulb_state = bulb^1 if steps % 2 else bulb

        print(current_bulb_state, A)
        if current_bulb_state == 0:
            steps += 1

    return steps

b = [ 1, 1, 0, 0, 1, 1, 0, 0, 1 ]
print(bulbs(b))
