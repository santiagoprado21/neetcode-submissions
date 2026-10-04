class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + "#" + i
        return encoded 


    def decode(self, s: str) -> List[str]:
        decoded = s
        result = []

        while decoded.find("#") != -1:
            
            k = decoded.find("#")
            lenght = int(decoded[:k])
            word = decoded[k+1:k+1+lenght]

            result.append(word)

            decoded = decoded[k+1+lenght:]

        return result 