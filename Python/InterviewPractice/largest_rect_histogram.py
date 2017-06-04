

def find_largest_rect(hist):
    bars = len(hist)
    stack = []
    i = 0
    max_area = None
    print(hist)
    while i < bars:
        print(i, stack, max_area)
        if not stack or hist[stack[-1]] <= hist[i]:
            stack.append(i)
            i += 1
        else:
            popped = stack.pop()
            area = hist[popped] * ( i if len(stack) == 0 else i-stack[-1]-1)
            print('Pop:', popped, i, area)
            if not max_area or area > max_area:
                max_area = area

    while stack:
        print(i, stack, max_area)
        popped = stack.pop()
        area = hist[popped] * ( i if len(stack) == 0 else i-stack[-1]-1)
        if not max_area or area > max_area:
            max_area = area
    return max_area


histogram = [6, 2, 5, 4, 5, 1, 6]
print(find_largest_rect(histogram))
