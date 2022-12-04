class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        x = sentence.split(" ")
        if(len(x)==1):
            if(x[0][0] == x[0][-1]):
                return True
            return False
        for i in range(len(x)-1):
            if(x[i][len(x[i])-1])!= x[i+1][0]:
                return False
            if(x[-1][-1]!= x[0][0]):
                return False
        return True