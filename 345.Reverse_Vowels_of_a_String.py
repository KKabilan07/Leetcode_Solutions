class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowels_list = [ch for ch in s if ch in vowels]
        result = []
        for ch in s:
            if ch in vowels:
                result.append(vowels_list.pop())
            else:
                result.append(ch)
        return ''.join(result)
        