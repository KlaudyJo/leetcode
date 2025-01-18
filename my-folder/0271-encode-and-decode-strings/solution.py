class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded = ""
        for w in strs:
            escaped = w.replace("#", "##")
            encoded += f"{len(escaped)}#{escaped}"


        return encoded
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # 5#hello5#world
        decoded = []
        i = 0
        while i < len(s):
            j = s.find("#", i) 
            length = int(s[i:j]) 
            word = s[j+1:j+length+1] 
            decode = word.replace("##", "#")
            decoded.append(decode)
            i = j + length + 1

        return decoded
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
