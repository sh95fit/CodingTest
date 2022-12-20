def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels :
        if vowel in my_string :
            my_string = my_string.replace(vowel, "")
    return my_string