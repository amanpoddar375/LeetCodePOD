class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        min_unfairness = float('inf')
        counts = [0] * k

        def backtrack(cookie_number, cookies, counts, k):
            nonlocal min_unfairness

            if cookie_number == len(cookies):
                maximum = max(counts)
                min_unfairness = min(min_unfairness, maximum)
                return

            for i in range(k):
                counts[i] += cookies[cookie_number]
                backtrack(cookie_number + 1, cookies, counts, k)
                counts[i] -= cookies[cookie_number]
                if counts[i] == 0:
                    break

        backtrack(0, cookies, counts, k)
        return min_unfairness

# TC : O(k^N), where N is the number of cookies.
# SC : O(N), where N is the number of cookies.