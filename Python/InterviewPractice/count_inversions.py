
def merge(a,b, half, start):
    len_a = len(a)
    len_b = len(b)
    i = j = inv = 0

    merged = []
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            inv += len_a - i
            # print(inv, half, start, i)
            j += 1

    merged += a[i:]
    merged += b[j:]

    return merged, inv

def sort(arr, inversions, orig_start):
    if len(arr) <= 1:
        return arr, inversions

    half = len(arr) // 2

    a, inversions = sort(arr[:half], inversions, orig_start)
    b, inversions = sort(arr[half:], inversions, half)

    merged, i  = merge(a,b, half, orig_start)
    return merged, inversions + i



def countInversions(a):

    arr, inv = sort(a, 0, 0)
    return inv

a = [468, 335, 1, 170, 225, 479, 359, 463, 465, 206, 146, 282, 328, 462, 492, 496, 443, 328, 437, 392, 105, 403, 154, 293, 383, 422, 217, 219, 396, 448, 227, 272, 39, 370, 413, 168, 300, 36, 395, 204, 312, 323]
print(countInversions(a))
