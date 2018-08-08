class Solution:
    """
    @param a: a string
    @param b: a string
    @return: a string representing their multiplication
    """
    def complexNumberMultiply(self, a, b):
        # Write your code here
        lis_a, lis_b = a.split("+"), b.split("+")
        lis_a[1], lis_b[1] = int(lis_a[1][:-1]), int(lis_b[1][:-1])
        lis_a[0], lis_b[0] = int(lis_a[0]), int(lis_b[0])
        
        multiply = lambda x,y: (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
        real, imag = multiply(lis_a, lis_b)
        return str(real)+"+"+str(imag)+"i"
    