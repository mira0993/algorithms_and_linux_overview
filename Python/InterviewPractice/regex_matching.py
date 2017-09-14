'''
Implement regular expression matching with support for '.' and '*',
given the following guidelines:

'.' Matches any single character.
'*' Matches zero or more of the element that comes before it.

The matching should cover the entire input string s. If the pattern p
matches the input string s, return true, otherwise return false.

Example

For s = "bb" and p = "b", the output should be False
For s = "zab" and p = "z.*", the output should be True
For s = "caab" and p = "d*c*x*a*b", the output should be True

  - z a b
- t f f f
d f
* f
c
*
x
*
a
*
b
'''

def regex_match(s, p):
    '''
if next is *:
    match 0 or more
    match this and more

if is *:
    if not match:
        ret False
    match again
    or go to next
    '''

    def match(s, p, i, j):
        if j == 25:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>', i)
        if j >=len(p) and i < len(s):
            return False

        if i >= len(s):
            if j >=len(p):
                return True

        ret = False
        if p[j] == '*':
            if i < len(s) and (s[i] == p[j-1] or p[j-1] == '.'):
                print('In *. Move s',i,j)
                ret |= match(s, p, i+1, j)
                if not ret:
                    print('In *. Move both',i,j)
                    ret |= match(s, p, i+1, j+1)
                    if not ret and p[j-1] == '.':
                        print('IS POINT', i, j)
                        ret |= match(s, p, i, j+1)
            else:
                print('In *. Move p',i,j)
                ret |= match(s, p, i, j+1)
        else:
            if j < len(p)-1 and p[j+1] == '*':
                print('ignore next *',i,j)
                ret |= match(s, p, i, j+2)
            if not ret and i < len(s) and (s[i] == p[j] or p[j] == '.'):
                print('move both',i,j)
                ret |= match(s, p, i+1, j+1)
        # print(ret, s, p, i ,j)
        return ret
    return match(s,p,0,0)


input_str = 'aasdfasdfasdfasdfas'
regex = 'aasdf.*asdf.*asdf.*asdf.*s'

print(regex_match(input_str, regex))
