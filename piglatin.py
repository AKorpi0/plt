
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
            elif word[0] not in 'aeiouAEIOU' and word[1] in 'aeiouAEIOU':
                # Handling single consonant start
                return word[1:] + word[0] + 'ay'
        return None

