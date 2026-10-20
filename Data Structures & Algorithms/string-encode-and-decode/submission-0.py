class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string = ""
        for word in strs:
            encoded_string = encoded_string + str(len(word)) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        #  4#ebin4#homo
        number = ""
        words = []
        i = 0
        length = 0
        while i < len(s):
            if s[i] == "#":

                i += 1
                length = int(number)
                words.append(s[i: i+length]) 
                i += length
                number = "" 
                continue
            number += s[i]
            i += 1

        return words