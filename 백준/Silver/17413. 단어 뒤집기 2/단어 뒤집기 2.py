def reverse_words_in_string(S):
    result = []
    word = []
    inside_tag = False
    
    for i in range(len(S)):
        if S[i] == '<':  
            if word:  
                result.append(''.join(word[::-1]))
                word = []

            inside_tag = True
            result.append('<')

        elif S[i] == '>':  
            inside_tag = False
            result.append('>')

        elif inside_tag:  
            result.append(S[i])

        else:  
            if S[i] == ' ':
                if word:  
                    result.append(''.join(word[::-1]))
                    word = []
                    
                result.append(' ')

            else:
                word.append(S[i])
       
    if word:
        result.append(''.join(word[::-1]))
   
    return ''.join(result)

S = input().strip()

print(reverse_words_in_string(S))

