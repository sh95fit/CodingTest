def solution(letter):
    answer = ''
    letter = letter.split()
    morse = { 
        '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
        '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
        '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
        '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
        '-.--':'y','--..':'z'
    }
    
    for key, value in morse.items() :
        for i in range(len(letter)) :
            if key == letter[i] :
                letter[i] = value
    return ''.join(letter)