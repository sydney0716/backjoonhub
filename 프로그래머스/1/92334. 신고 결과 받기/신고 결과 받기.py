def solution(id_list, reports, k):
    answer = []
    organized_reports = list(set(reports))
    report_list = dict.fromkeys(id_list, 0)
    mail_list = dict.fromkeys(id_list, 0)
    temp_list = {user_id: [] for user_id in id_list}
    
    for report in organized_reports:
        user_id, reported_user_id = report.split()
        
        report_list[reported_user_id] += 1
        reported_count = report_list[reported_user_id]
        
        if reported_count < k:
            temp_list[reported_user_id].append(user_id)
        elif reported_count == k:
            mail_list[user_id] += 1

            for temp in temp_list[reported_user_id]:
                mail_list[temp] += 1
        else:
            mail_list[user_id] += 1
            
            
    for _, mail in mail_list.items():
        answer.append(mail)
        
    return answer