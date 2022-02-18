class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
    
        for word in anagrams:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())
