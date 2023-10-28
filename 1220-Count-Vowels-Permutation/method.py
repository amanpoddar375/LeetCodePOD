class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        # Initialize a dictionary to store the results of subproblems
        memo = {}

        def countStrings(s, n):
            if n == 0:
                return 1
            if (s, n) in memo:
                return memo[(s, n)]

            count = 0
            if s == '':
                count = (
                    countStrings('a', n - 1) + 
                    countStrings('e', n - 1) + 
                    countStrings('i', n - 1) + 
                    countStrings('o', n - 1) + 
                    countStrings('u', n - 1)
                )
            else:
                if s == 'a':
                    count = countStrings('e', n - 1)
                elif s == 'e':
                    count = countStrings('a', n - 1) + countStrings('i', n - 1)
                elif s == 'i':
                    count = (
                        countStrings('a', n - 1) +
                        countStrings('e', n - 1) +
                        countStrings('o', n - 1) +
                        countStrings('u', n - 1)
                    )
                elif s == 'o':
                    count = countStrings('i', n - 1) + countStrings('u', n - 1)
                else:
                    count = countStrings('a', n - 1)

            memo[(s, n)] = count % MOD
            return memo[(s, n)]

        return countStrings('', n) % MOD
