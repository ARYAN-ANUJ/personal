class Solution:
    def decodeAtIndex(self, encodedString: str, k: int) -> str:
        character_lengths = [0]  

        for i in range(len(encodedString)):
            if encodedString[i].isdigit():
                length = character_lengths[-1] * int(encodedString[i])
                character_lengths.append(length)
            else:
                length = character_lengths[-1] + 1
                character_lengths.append(length)

       
        # ln = len(character_lengths)
        
        
        while character_lengths:
            k %= character_lengths[-1]  
            
            ln =len(character_lengths)-1
            
            if k == 0 and encodedString[ln - 1].isalpha():
                return encodedString[ln - 1]

            character_lengths.pop()

        return ""