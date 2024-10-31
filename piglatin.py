
class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if not self._phrase:
            return "nil"
        words = self._phrase.split()
        if len(words) == 1 and words[0][0] in 'aeiouyAEIOUY':
            if words[0][-1] in 'aeiouAEIOU':
                return words[0] + 'yay'
            elif words[0][-1] in 'yY':
                return words[0]+ 'nay'
            return words[0] + 'ay'
        return None

