
class PigLatin:
    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        start=""
        end=""
        if not self._phrase:
            return "nil"
        words = self._phrase.split()
        translated_words = []
        for word in words:
            if "-" in word:
                split = word.split("-")
            else:
                split = [word]
            for word in split:
                upper = False
                title = False
                if word[0] in ".,:;()?!'":
                    start = word[0]
                    word = word[1:]
                if word[-1] in ".,:;()?!'":
                    end = word[-1]
                    word = word[:-1]
                if word[0].isupper():
                    upper = True
                if word.isupper():
                    title=True
                if word[0] in 'aeiouAEIOU':
                    if word[-1] in 'aeiouAEIOU':
                        translated_words.append(start+word + 'yay'+end)
                    elif word[-1] in 'yY':
                        translated_words.append(start+word + 'nay'+end)
                    else:
                        translated_words.append(start+word + 'ay'+end)
                else:
                    if all(c not in 'aeiouAEIOU' for c in word[1:]):
                        translated_words.append(start+word + 'ay'+end)
                    else:
                        first_vowel = next((i for i, c in enumerate(word) if c in 'aeiouAEIOU'), len(word))
                        translated_words.append(start+word[first_vowel:] + word[:first_vowel] + 'ay'+end)
                if upper:
                    translated_words.append(translated_words.pop().capitalize())
                if title:
                    translated_words.append(translated_words.pop().upper())

            if len(split) > 1:
                word2=translated_words.pop()
                word1=translated_words.pop()
                translated_words.append(word1+"-"+word2)
        return ' '.join(translated_words)

