class Time():
    def __init__(self, n):
        self.hour = n // 100
        self.minute = n % 100

    def add(self, n):
        self.minute += n

        if self.minute >= 60:
            add_hours = self.minute // 60
            self.hour += add_hours
            self.minute %= 60
            self.hour %= 24
        return self
    
    def compare(self, compare_time):
        if (self.hour, self.minute) > (compare_time.hour, compare_time.minute):
            return 1
        elif (self.hour, self.minute) < (compare_time.hour, compare_time.minute):
            return 2
        else:
            return 0

def solution(schedules, timelogs, startday):
    worker_num = len(schedules)
    answer = worker_num
    for i in range(worker_num):
        for day in range(7):
            set_time = Time(schedules[i]).add(10)
            if day == (6 - startday) % 7 or day == (7 - startday) % 7 :
                continue
            else:
                comute_time = Time(timelogs[i][day])
                if set_time.compare(Time(timelogs[i][day])) == 2:
                    answer -= 1
                    break
    return answer