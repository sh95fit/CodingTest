from itertools import permutations

def get_strikes_and_balls(secret, guess):
    strike = sum(1 for i in range(3) if secret[i] == guess[i])
    ball = sum(1 for i in range(3) if secret[i] != guess[i] and guess[i] in secret)

    return strike, ball

def solve():  
    possible_answers = [''.join(map(str, p)) for p in permutations(range(1, 10), 3)]
       
    N = int(input().strip())       
   
    for _ in range(N):
        guess, strike, ball = input().split()
        strike, ball = int(strike), int(ball)
               
        new_possible_answers = []
        
        for answer in possible_answers:
            s, b = get_strikes_and_balls(answer, guess)

            if s == strike and b == ball:
                new_possible_answers.append(answer)
         
        possible_answers = new_possible_answers
 
    print(len(possible_answers))

solve()

