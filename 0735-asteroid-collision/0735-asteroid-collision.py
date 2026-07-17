class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids :
            if not stack or  i * stack[-1] > 0 or i>0:
                stack.append(i)
            else :
                flag = 0
                while stack and i * stack[-1] <0 :
                    if abs(i) > abs(stack[-1]) :
                        stack.pop()
                    elif abs(i) == abs(stack[-1]) :
                        stack.pop()
                        flag =1
                        break
                    else :
                        flag = 1
                        break
                if flag == 0:
                    stack.append(i) 
        return stack

# same-direction → no fight, just stack
# new right-mover → never fights on arrival
# new left-mover meeting a right-mover on top → fight, possibly multiple times as it pops through the stack
# new left-mover meeting an empty stack or a left-mover on top → no fight, just stack   
       

