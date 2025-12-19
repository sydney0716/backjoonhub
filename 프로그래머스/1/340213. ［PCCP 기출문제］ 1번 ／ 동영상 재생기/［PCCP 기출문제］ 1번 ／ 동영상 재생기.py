class Time():
    def __init__(self, time):
        self.mm = int(time[0:2])
        self.ss = int(time[3:5])
    
    def __str__(self):
        return f"{self.mm:02d}:{self.ss:02d}"
    
    def __lt__(self, other):
        return (self.mm, self.ss) < (other.mm, other.ss)
    
    def __le__(self, other):
        return (self.mm, self.ss) <= (other.mm, other.ss)
    
    
    def add(self, time):
        self.mm += time.mm
        self.ss += time.ss
        if self.ss >= 60:
            self.mm += self.ss // 60
            self.ss %= 60
        return self
    
    def subtract(self, time):
        self.mm -= time.mm
        self.ss -= time.ss
        if self.ss < 0:
            self.mm -= 1
            self.ss %= 60
        return self

def isInOpening(cur, start, end):
    if start <= cur and cur <= end:
        return True
    else:
        return False

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    zero_time = Time("00:00")
    ten_time = Time("00:10")
    video_length = Time(video_len)
    current_time = Time(pos)
    op_start_time = Time(op_start)
    op_end_time = Time(op_end)
    
    if isInOpening(current_time, op_start_time, op_end_time):
        current_time = op_end_time
        
    for command in commands:
        if command == "prev":
            current_time.subtract(ten_time)
            
            if current_time < zero_time:
                current_time = Time("00:00")
                
        if command == "next":
            current_time.add(ten_time)
            if  video_length < current_time:
                current_time = Time(video_len)

        if isInOpening(current_time, op_start_time, op_end_time):
            current_time = Time(str(op_end_time))
    
    return str(current_time)