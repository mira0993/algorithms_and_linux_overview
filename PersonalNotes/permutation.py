'''
Find all the permutations of a given string
'''

def permutation(word, index=0):
    
    if index == len(word):
        print("".join(word))

    else:
        for i in range(index, len(word)):
            word[index], word[i] = word[i], word[index]
            permutation(word, index+1)
            word[index], word[i] = word[i], word[index]


string = list(input('Find all permutations:'))
permutation(string)

