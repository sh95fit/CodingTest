word = input().upper() 
frequency = {} 

for char in word:
    if char.isalpha(): 
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

max_frequency = max(frequency.values())  

max_chars = [char for char, freq in frequency.items() if freq == max_frequency]  

if len(max_chars) == 1: 
    print(max_chars[0])
else:  
    print("?")