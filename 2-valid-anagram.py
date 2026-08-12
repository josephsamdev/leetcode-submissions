# brute force solution 
def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t


# O(n) method - which is faster than O(n log n) in the above
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1
        for letter in t:
            count[letter] = count.get(letter, 0) - 1    

        return all(v == 0 for v in count.values())