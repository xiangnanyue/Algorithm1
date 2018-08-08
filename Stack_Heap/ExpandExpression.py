class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        for i in s:
            if i == "]":
                exp = []
                e = stack.pop()
                while e != "[":
                    exp = [e] + exp
                    e = stack.pop()
                num = ""
                e = stack[-1]
                while e >= "0" and e <= "9":
                    num = stack.pop() + num
                    if len(stack) == 0:
                        break
                    e = stack[-1]
                num = int(num)
                for j in range(num):
                    stack += exp
            else:
                stack.append(i)
        return "".join(stack)
                     
             