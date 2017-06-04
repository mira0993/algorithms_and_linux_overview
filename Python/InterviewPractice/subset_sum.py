


def subset_sum(arr):

    a = []
    a_sum = 0
    b = []
    b_sum = 0

    arr.sort()
    i = len(arr)-1

    while i >= 0:
        if a_sum < b_sum:
            a.append(arr[i])
            a_sum += arr[i]
        else:
            b.append(arr[i])
            b_sum += arr[i]
        i-=1

    print(a_sum, a)
    print(b_sum, b)




arr = [87, 56, 43, 91, 27, 65, 59, 36, 32, 51, 37, 28, 75, 7, 74]
subset_sum(arr)

