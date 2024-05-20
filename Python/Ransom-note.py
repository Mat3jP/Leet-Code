class Solution:
    #def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    def canConstruct(sef, ransomNote, magazine):
        for char in ransomNote:
            if char not in magazine:
                return False
            else:
                magazine = magazine.replace(char,"",1)

        return True