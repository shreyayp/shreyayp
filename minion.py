def minion_game(string):
 def minion_game(string):
    
    kevin_score = 0
    stuart_score = 0

    
    vowels = "AEIOU"

    
    for i in range(len(string)):
        if string[i] in vowels:
            
            kevin_score += len(string) - i
        else:
            
            stuart_score += len(string) - i

   
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


s = input("Enter a string: ")
minion_game(s)


if __name__ == '__main__':
    s = input()
    minion_game(s)