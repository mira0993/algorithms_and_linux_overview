class Solution:
    # @param A : string
    # @return an integer
    def cnttrue(self, A):

        def solution(expr, start, end):
            if start == end:
                if expr[start] == 'T':
                    return 1,0
                else:
                    return 0,1

            if end < start:
                return 0

            valid = 0
            invalid = 0

            for index in range(start, end+1):
                if expr[index] not in ('T', 'F'):
                    t_left, f_left = solution(expr, start, index-1)
                    t_right, f_right = solution(expr, index+1, end)

                    left_all = t_left + f_left
                    right_all = t_right + f_right

                    op = expr[index]

                    if op == '|':
                        valid += (t_left * t_right) + (t_left * f_right) + (f_left * t_right)
                        invalid += (f_left * f_right)
                    elif op == '&':
                        valid += (t_left * t_right)
                        invalid += ((f_left * f_right) + (t_left * f_right) + (f_left * t_right))
                    elif op == '^':
                        valid += (t_left * f_right) + (f_left * t_right)
                        invalid += (f_left * f_right) + (t_left * t_right)
                    if start == 0 and end == 10:
                        print(expr[index: end+1], index, start, end, 'ret=>', valid, invalid)
            return valid, invalid

        return solution(A, 0, len(A)-1)[0]

expression = 'F&F&F&T^T|F'
print(expression)
print(Solution().cnttrue(expression))
