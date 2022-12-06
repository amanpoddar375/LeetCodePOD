class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        #as skill of each team should be equal, we took target skill as smallest + largest
        target = skill[0] + skill[-1]
        sum = 0
        for i in range(n//2):
            #checking if the target skill can be used to made the proper team from the given array
            if target != skill[i] + skill[n-i-1]:
                return -1
            sum += skill[i] * skill[n-i-1]
        return sum
