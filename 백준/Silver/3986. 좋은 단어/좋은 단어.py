def is_good_word(word):
    stack = []    

    for char in word:
        if not stack:
            stack.append(char)

        else:
            if stack[-1] == char:
                stack.pop() 
            else:
                stack.append(char)      
   
    return len(stack) == 0

def count_good_words(words):
    good_word_count = 0
    
    for word in words:
        if is_good_word(word):
            good_word_count += 1
    
    return good_word_count

N = int(input())
words = [input().strip() for _ in range(N)]

print(count_good_words(words))

