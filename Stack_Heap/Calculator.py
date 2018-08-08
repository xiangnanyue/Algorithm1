"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.
"""
class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        # good for all form
        values = []
        operators = []
        l = len(s)
        i = 0
        num = ""
        while i < l:
            op = s[i]
            if op == " ":
                i+=1
                continue
            elif op == "(":
                values.append(op)
            elif op == "+" or op == "-":
                operators.append(op)
            elif op >= "0" and op <= "9":
                num += op
                while i+1 < l and s[i+1] >= "0" and s[i+1]<= "9":
                    i += 1
                    num += s[i]
                values.append(int(num))
                num = ""
            elif op == ")":
                values[-1] = values.pop()
            while len(values) > 1 and values[-2] != "(" and values[-1] != "(" and len(operators)>=1:
                vfirst = int(values.pop())
                vsecond = int(values.pop())
                operator = operators.pop()
                if operator == "-":
                    values.append(vsecond-vfirst)
                elif operator == "+":
                    values.append(vsecond+vfirst)
            i += 1
            #print(values, operators)
        return values[0]

    def calculate2(self, s):
        # Write your code here
        # this only fit the form: "(5-(3-(1 + 1))) " yet not 5-3-1+1
        values = []
        operators = []
        l = len(s)
        i = 0
        num = ""
        while i < l:
            op = s[i]
            if op == " " or op == "(":
                pass
            elif op == "+" or op == "-" :
                operators.append(op)
            elif op == ")":
                vfirst = int(values.pop())
                vsecond = int(values.pop())
                operator = operators.pop()
                if operator == "-":
                    values.append(vsecond-vfirst)
                elif operator == "+":
                    values.append(vsecond+vfirst)
            elif op >= "0" and op <= "9":
                num += op
                while i+1 < l and s[i+1] >= "0" and s[i+1]<= "9":
                    i += 1
                    num += s[i]
                values.append(int(num))
                num = ""
            i += 1
            print(values, operators)
        return values[0]

        def calculate3(self,s):
            """
            a recursive method
            http://www.cnblogs.com/grandyang/p/8873471.html

            to explicitely construct an algebraic binary expression tree
            https://en.wikipedia.org/wiki/Binary_expression_tree
            """
            pass

class ExpressionTree:
    """
    @param: expression: A string array
    @return: The root of expression tree

    more complicated question is: how to translate to inverse-poland expression.
    https://zh.wikipedia.org/wiki/%E8%B0%83%E5%BA%A6%E5%9C%BA%E7%AE%97%E6%B3%95

    思路1：调度场算法，将中缀表达式改写成后缀表达式
    思路2: 类似的，运算符号栈每次遇到 ）都往前找到（ 进行 表达式运算
          表达式运算中，先进行优先级高的运算。
    """
    def build(self, expression):
        # write your code here
        
    def expr(self, expression):
        # first implement a non-paranthese one 
        # with only + -, * /
        

class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value

    https://en.wikipedia.org/wiki/Reverse_Polish_notation
    """
    def evalRPN(self, tokens):
        # write your code here
        stack = []
        #stackop = []
        while len(tokens) > 0:
            newop = tokens.pop(0)
            if newop not in "+-*/":
                stack.append(int(newop))
                continue
            first = stack.pop()
            second = stack.pop()
            if newop == "+":
                stack.append(int(first + second))
            elif newop == "-":
                stack.append(int(second - first))
            elif newop == "/":
                stack.append(int(second / first))
            elif newop == "*":
                stack.append(int(second * first))
        return stack[0]

