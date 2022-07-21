for i in range(1, int(input())+1):
    word = input()
    mid = len(word)//2
    for j in range(mid):
        if len(word)%2 != 0 and (word[mid+(j+1)] == word[mid-(j+1)]):
                print(f'#{i} {1}')
                break
        else:
            if word[j] == word[(len(word)-1)-j]:
                print(f'#{i} {1}')
                break        
        print(f'#{i} {0}')
        break