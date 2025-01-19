from process import Process

class PriorityScheduler:
    def __init__(self, mode="Non-Preemptive"):
        self.processes = []
        self.mode = mode  # Either "Preemptive" or "Non-Preemptive"
        self.avg_waiting_time = 0
        self.avg_turnaround_time = 0
        self.avg_response_time = 0
        self.gantt_chart = []  # To store the timeline for Gantt chart visualization

    def add_process(self, arrival_time, burst_time, priority):
        self.processes.append(Process(arrival_time, burst_time, priority))

    def calculate(self):
        if self.mode == "Non-Preemptive":
            self.calculate_non_preemptive()
        else:
            self.calculate_preemptive()

    def calculate_non_preemptive(self):
        self.processes.sort(key=lambda x: (x.arrival_time, x.priority))
        time = 0
        for process in self.processes:
            if time < process.arrival_time:
                self.gantt_chart.append("Idle")
                time = process.arrival_time

            process.start_time = time
            process.end_time = time + process.burst_time
            process.waiting_time = process.start_time - process.arrival_time
            process.turnaround_time = process.end_time - process.arrival_time
            process.response_time = process.start_time - process.arrival_time
            self.gantt_chart.extend([f"P{self.processes.index(process) + 1}"] * process.burst_time)

            time = process.end_time

        self.calculate_averages()

    def calculate_preemptive(self):
        self.processes.sort(key=lambda x: (x.arrival_time, x.priority))
        time = 0
        completed = 0
        n = len(self.processes)

        while completed < n:
            ready_queue = [p for p in self.processes if p.arrival_time <= time and p.remaining_time > 0]
            ready_queue.sort(key=lambda x: (x.priority, x.arrival_time))

            if ready_queue:
                current_process = ready_queue[0]
                if current_process.start_time == -1:
                    current_process.start_time = time
                time += 1
                current_process.remaining_time -= 1
                self.gantt_chart.append(f"P{self.processes.index(current_process) + 1}")

                if current_process.remaining_time == 0:
                    current_process.end_time = time
                    current_process.turnaround_time = current_process.end_time - current_process.arrival_time
                    current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                    if current_process.response_time == -1:
                        current_process.response_time = current_process.start_time - current_process.arrival_time
                    completed += 1
            else:
                self.gantt_chart.append("Idle")
                time += 1

        self.calculate_averages()

    def calculate_averages(self):
        n = len(self.processes)
        self.avg_waiting_time = sum(p.waiting_time for p in self.processes) / n
        self.avg_turnaround_time = sum(p.turnaround_time for p in self.processes) / n
        self.avg_response_time = sum(p.response_time for p in self.processes) / n
