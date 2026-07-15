class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =  []
        answer = [0]*len(temperatures)
        top = -1
        for new in range(len(temperatures)):
            while stack and temperatures[new] > temperatures[stack[top]] :
                    answer[stack[top]] = new - stack[top]
                    top-=1
                    stack.pop()
            top+=1
            stack.append(new)
        if not stack :
            answer[stack[top]] = 0
            top-=1
        return answer




             