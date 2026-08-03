class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams={}
        for word in strs:
            count_signature=self.freqCounter(word)
            if count_signature not in anagrams:
                anagrams[count_signature] = []
            
            anagrams[count_signature].append(word)
        group = []
        for values in anagrams.values():
            group.append(values)
            
        return group

        

    def freqCounter(self, word: str):
        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord('a')] += 1

        return tuple(count)