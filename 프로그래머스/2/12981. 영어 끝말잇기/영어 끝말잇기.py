def game(word_array):
    for i, word in enumerate(word_array):
        if i != 0:
            if word[0] != word_array[i - 1][-1]:
                return i
        for l in range(i):
            if word == word_array[l]:
                return i
            
    return -1
            
def solution(n, words):
    answer = [0, 0]

    turns = len(words)

    result = game(words)
    if result != -1:
        answer[0] = result % n + 1
        answer[1] = result // n + 1
        
        
    return answer