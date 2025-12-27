def solution(players, m, k):
    answer = 0
    current_server = 1
    server_return = [0] * 24 
    for time in range(24):
        players_by_time = players[time]
        current_server -= server_return[time]
        excess_players = players_by_time - (m * current_server - 1)
        
        if excess_players <= 0:
            continue
        
        
        expand_server_count = (excess_players - 1) // m + 1
        current_server += expand_server_count
        answer += expand_server_count
        
        if time + k < 24:
            server_return[time + k] += expand_server_count

    return answer