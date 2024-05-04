if __name__ == '__main__':
    n = int(input())  
    scores = list(map(int, input().split()))  

    
    unique_scores = sorted(set(scores))

    
    runner_up_score = unique_scores[-2]

    print(runner_up_score)