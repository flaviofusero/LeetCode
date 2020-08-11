import logging
class Solution:
    def countCharacters(self, words, chars) -> int:
        counter = 0
        for i in range(len(words)):
            if len(words[i]) <= len(chars):
                notGood = 0
                chars_copy = chars[:]
                for j in range(len(words[i])):
                    if words[i][j] in chars_copy:
                        chars_copy = chars_copy.replace(words[i][j], "", 1)
                    else:
                        notGood = 1
                        break
                if notGood == 0:
                    counter += len(words[i])
        return counter


s = Solution()
logging.warning(s.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))