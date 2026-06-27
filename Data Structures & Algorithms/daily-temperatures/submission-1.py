class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []    # this is a nested list for --> [value, index]

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:

                stack_value, stack_index = stack.pop()
                res[stack_index] = i - stack_index

            stack.append([t , i])
            
        return res

        