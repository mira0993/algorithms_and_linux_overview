'''
Write code to find all Palindromes in a given sample string.
Example: "pop this tacocat seems nice at noon"
"pop", "s tacocat s", " tacocat ", "tacocat", "acoca", "coc", "noon"
'''

def find_palindromes_brute_force(sentence):
    pals = []
    len_s = len(sentence)
    comparisons = 0

    for x in range(len_s-1):
        for y in range(x+1, len_s):

            i = x
            j = y

            while j > i:
                comparisons += 1
                if sentence[i] == sentence[j]:
                    j-=1
                    i+=1
                else:
                    break
            if j <= i:
                pals.append(sentence[x:y+1])
    print(comparisons, len_s)
    print(pals)
    return pals


def find_better(s):
    pals = []
    comparisons = 0
    pivot = 0
    while pivot < len(s):
        i = pivot - 1
        j = pivot + 1

        while i >= 0 and j < len(s):
            comparisons += 1
            if s[i] != s[j]:
                break
            pals.append(s[i:j+1])
            i -= 1
            j += 1

        i = pivot
        j = pivot + 1

        while i >= 0 and j < len(s):
            comparisons += 1
            if s[i] != s[j]:
                break
            pals.append(s[i:j+1])
            i -= 1
            j += 1

        pivot = j

    print('Comparisons', comparisons)
    return pals



s = 'pop this tacocat seems nice at noon'
print(find_better(s))
