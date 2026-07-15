class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # answer = [0]*len(temperatures)
        # for i in range(len(temperatures)):
        #     j = i+1
        #     pos = 1
        #     while j<len(temperatures):
        #         if temperatures[j] > temperatures[i] :
        #             answer[i] = pos
        #             break
        #         pos+=1
        #         j+=1
        #     else :
        #         answer[i] = 0
        # return answer
        stack =  []
        answer = [0]*len(temperatures)
        top = -1
        for new in range(len(temperatures)):
            while stack and temperatures[new] > temperatures[stack[top]] :
                    answer[stack[top]] = new - stack[top]
                    top-=1
                    stack.pop()
            else :
               top+=1
               stack.append(new)
        if not stack :
            answer[stack[top]] = 0
            top-=1
        return answer




             