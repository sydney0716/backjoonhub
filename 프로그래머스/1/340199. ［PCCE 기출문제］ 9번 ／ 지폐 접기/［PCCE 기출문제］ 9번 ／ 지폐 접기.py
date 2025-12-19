def isFit(wallet_size, bill_size):
    wallet_min = min(wallet_size)
    wallet_max = max(wallet_size)
    
    bill_min = min(bill_size)
    bill_max = max(bill_size)
    
    
    if wallet_min >= bill_min and wallet_max >= bill_max:
        return True
    else:
        return False
    

def solution(wallet, bill):
    answer = 0
    
    while not isFit(wallet, bill):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
    return answer