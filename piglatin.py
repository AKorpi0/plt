
class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"
        words = self._phrase.split()
        if len(words) == 1:
            word = words[0]
            if word[0] in 'aeiouAEIOU':
                if word[-1] in 'aeiouAEIOU':
                    return word + 'yay'
                elif word[-1] in 'yY':
                    return word + 'nay'
                return word + 'ay'
            elif word[0] not in 'aeiouAEIOU':
                if all(c not in 'aeiouAEIOU' for c in word[1:]):
                    return word + 'ay'
                first_vowel = next((i for i, c in enumerate(word) if c in 'aeiouAEIOU'), len(word))
                return word[first_vowel:] + word[:first_vowel] + 'ay'
        return None

