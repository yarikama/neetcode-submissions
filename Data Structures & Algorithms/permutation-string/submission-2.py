class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = [0] * 26
        for c in s1:
            counter1[ord(c) - ord("a")] += 1

        counter2 = [0] * 26
        for i in range(len(s1)):
            print(i)
            print(s2[i])
            counter2[ord(s2[i]) - ord("a")] += 1
        
        L, R = 0, len(s1)-1
        while R < len(s2)-1:
            if counter1 == counter2:
                return True
            counter2[ord(s2[L]) - ord("a")] -= 1
            L += 1
            R += 1
            counter2[ord(s2[R]) - ord("a")] += 1
            

        return False