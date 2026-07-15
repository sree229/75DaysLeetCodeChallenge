class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =  []
        answer = [0]*len(temperatures)
        for new in range(len(temperatures)):
            while stack and temperatures[new] > temperatures[stack[-1]] :
                    answer[stack[-1]] = new - stack[-1]
                    stack.pop()
            stack.append(new)
        return answer




             