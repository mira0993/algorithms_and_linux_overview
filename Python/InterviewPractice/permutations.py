from math import factorial

def permutations(word):
    '''
    Print all the permutations of a given string. Order no matter.
    '''

    def _permutations(arr, index):
        if index >= len(arr):
            print(''.join(arr))
            return

        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i], arr[index]
            _permutations(arr, index+1)
            arr[index], arr[i] = arr[i], arr[index]

    _permutations(list(word), 0)

def find_next_higher_permutation(arr):
    '''
    1. Take the previously printed permutation and find the rightmost
    character in it, which is smaller than its next character.
    Let us call this character as ‘first character’.

    2. Now find the ceiling of the ‘first character’.
    Ceiling is the smallest character on right of ‘first character’,
    which is greater than ‘first character’.
    Let us call the ceil character as ‘second character’.

    3. Swap the two characters found in above 2 steps.

    4. Sort the substring (in non-decreasing order) after the original
    index of ‘first character’.
    '''

    first = len(arr) - 2
    while first >= 0 and arr[first] > arr[first+1]:
        first -= 1

    if first < 0:
        return None

    second = - 1
    for index in range(first+1, len(arr)):
        if arr[index] > arr[first]:
            if second == -1 or arr[second] > arr[index]:
                second = index

    if second < 0:
        return None

    arr[first], arr[second] = arr[second], arr[first]

    return arr[0:first+1] + sorted(arr[first+1:])

def sorted_permutations(word):
    '''
    Print all the permutatins of a given string in lexicographical order.

    1. Sort the given string in non-decreasing order and print it.
    The first permutation is always the string sorted in non-decreasing order.

    2. Start generating next higher permutation. Do it until next higher
    permutation is not possible
    '''

    list_word = list(word)
    list_word.sort()
    count =  0
    while list_word:
        print(count, ''.join(list_word))
        list_word = find_next_higher_permutation(list_word)
        count += 1


def find_k_permutation(word, k_permutation):
    '''
    Given n and k, return the kth permutation sequence.
    '''
    list_word = sorted(list(word))
    permutation = []
    k = k_permutation - 1

    index = len(list_word) - 1

    while index >= 0:
        fact = factorial(index)
        subset = k//fact

        permutation.append(list_word[subset])
        list_word.pop(subset)
        k = k%fact

        index -= 1

    print(k_permutation, permutation)

word = 'abcd'
#sorted_permutations(word)
find_k_permutation(word, 19)
