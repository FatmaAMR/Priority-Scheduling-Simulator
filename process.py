class Process:
    def __init__(self, arrival_time, burst_time, priority):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.start_time = -1
        self.end_time = -1
        self.waiting_time = 0
        self.turnaround_time = 0
        self.response_time = -1
