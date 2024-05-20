class Solution:
    #def findArray(self, pref: List[int]) -> List[int]:
    def findArray(self, pref):
        prev = pref[0]
        for i in range(1,len(pref)):
            curr = pref[i]
            pref[i] = prev^pref[i]
            prev = curr
        return pref
        