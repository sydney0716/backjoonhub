def solution(citations):
    citations.sort(reverse=True)
    article_num = len(citations)
    answer = article_num
    
    for i in range(article_num):
        if citations[i] <= i:
            answer = i
            break
            
    return answer