def solution(babbling):
    answer = 0
    
    for bab in babbling:
        i = 0
        prev = ""
        bab_len = len(bab)
        available_flag = True
        while i < bab_len:
            # three alphabet
            if i + 2 < bab_len:
                word = bab[i : i + 3]
                if word != prev and (word == "aya" or word == "woo"):
                    prev = word
                    i += 3
                elif word[0:2] != prev and (word[0:2] == "ye" or word[0:2] == "ma"):
                    prev = word[0:2]
                    i += 2
                else:
                    available_flag = False
                    break
                    
            # two alphabet
            elif i + 1 < bab_len:
                word = bab[i : i + 2]
                
                if word != prev and (word == "ye" or word == "ma"):
                    prev = word
                    i += 2
                else:
                    available_flag = False
                    break
            # what if only one alphabet is left? -> false
            else:
                available_flag = False
                i += 1
            
        if available_flag:
            answer += 1
    
    return answer