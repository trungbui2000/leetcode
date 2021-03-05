# 1768. Merge Strings Alternately


def mergeAlternately(word1: str, word2: str) -> str:
    position_left = 0
    final_string = ""
    if (len(word1) > len(word2)):
        for i in range(0,len(word2)):
            final_string += (word1[i] + word2[i])
            position_left += 1
        final_string += word1[position_left:]
    elif (len(word1) < len(word2)):
        for i in range(0,len(word1)):
            final_string += (word1[i] + word2[i])
            position_left += 1
        final_string += word2[position_left:]
    else:
        for i in range(0,len(word1)):
            final_string += (word1[i] + word2[i])
    return final_string
        
            
word1 = "abc"
word2 = "def"
print(mergeAlternately(word1,word2))