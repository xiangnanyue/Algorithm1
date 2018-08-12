class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        # priority queue -- array implementation
        pq = [1]
        stack = []
        dic = {}
        i = 0
        while i < n:
            mim = pq.pop(0)
            for p in primes:
                newN = p*mim
                if dic.get(newN) is not None:
                    continue
                else:
                    dic[newN] = True
                    pq.append(newN)
                for j in range(len(pq)-1, 0, -1):
                    if pq[j] < pq[j-1]:
                        temp = pq[j]
                        pq[j] =pq[j-1]
                        pq[j-1] = temp
                    else:
                        break
            i += 1
            stack.append(mim)
        print(stack)
        return stack[-1]