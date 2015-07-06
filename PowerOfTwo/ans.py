class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        powers = []
        for i in range(0, 32):
            num = 2**i
            print num,
            powers.append(num)
        if n in powers:
            return True
        return False
