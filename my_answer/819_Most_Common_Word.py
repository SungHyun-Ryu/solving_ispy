class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_lower = []
        allowed_words = []

        words = re.sub(r'[^a-z]', ' ', paragraph.lower()).split()
        for word in banned:
            banned_lower.append(word.lower())


        for word in words:
            if not word in banned_lower:
                allowed_words.append(word)


        counter = collections.Counter(allowed_words)
        return counter.most_common(1)[0][0]
