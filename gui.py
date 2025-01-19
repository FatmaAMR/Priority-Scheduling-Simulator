import tkinter as tk
from tkinter import ttk
from scheduler import PriorityScheduler
from utils import get_blue_gradient
from tkinter import messagebox

class SchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Priority Scheduling")
        self.root.geometry("800x600")

        self.scheduler = PriorityScheduler()

        self.setup_gui()

    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Mode:").grid(row=0, column=0)
        self.mode_var = tk.StringVar(value="Non-Preemptive")
        mode_menu = ttk.Combobox(frame, textvariable=self.mode_var, values=["Non-Preemptive", "Preemptive"])
        mode_menu.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Arrival Time:").grid(row=1, column=0)
        self.arrival_time_entry = tk.Entry(frame)
        self.arrival_time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Burst Time:").grid(row=2, column=0)
        self.burst_time_entry = tk.Entry(frame)
        self.burst_time_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Priority:").grid(row=3, column=0)
        self.priority_entry = tk.Entry(frame)
        self.priority_entry.grid(row=3, column=1, padx=5, pady=5)

        add_button = tk.Button(frame, text="Add Process", command=self.add_process)
        add_button.grid(row=4, column=0, columnspan=2, pady=5)

        calculate_button = tk.Button(frame, text="Calculate", command=self.calculate)
        calculate_button.grid(row=5, column=0, columnspan=2, pady=5)

        gantt_button = tk.Button(frame, text="Show Gantt Chart", command=self.display_gantt_chart)
        gantt_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.process_list = tk.Text(self.root, width=80, height=10)
        self.process_list.pack(pady=10)

        self.results = tk.Label(self.root, text="", font=("Arial", 12))
        self.results.pack(pady=10)

    def add_process(self):
        try:
            arrival_time = int(self.arrival_time_entry.get())
            burst_time = int(self.burst_time_entry.get())
            priority = int(self.priority_entry.get())
            self.scheduler.add_process(arrival_time, burst_time, priority)

            self.process_list.insert(tk.END, f"Added Process - Arrival Time: {arrival_time}, Burst Time: {burst_time}, Priority: {priority}\n")
            self.arrival_time_entry.delete(0, tk.END)
            self.burst_time_entry.delete(0, tk.END)
            self.priority_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

    def calculate(self):
        self.scheduler.mode = self.mode_var.get()
        self.scheduler.calculate()
        self.display_results()

    def display_results(self):
        results_text = (
            f"Average Waiting Time: {self.scheduler.avg_waiting_time:.2f}\n"
            f"Average Turnaround Time: {self.scheduler.avg_turnaround_time:.2f}\n"
            f"Average Response Time: {self.scheduler.avg_response_time:.2f}"
        )
        self.results.config(text=results_text)

    def display_gantt_chart(self):
        # Create a new top-level window for the Gantt chart
        gantt_chart_window = tk.Toplevel(self.root)
        gantt_chart_window.title("Gantt Chart")
        gantt_chart_window.geometry("800x200")

        # Create a canvas for drawing the Gantt chart
        canvas = tk.Canvas(gantt_chart_window, bg="white")
        canvas.pack(fill=tk.BOTH, expand=True)

        # Clear any previous content on the canvas
        canvas.delete("all")

        # Adjust the canvas size dynamically based on the number of processes in the Gantt chart
        total_width = len(self.scheduler.gantt_chart) * 30  # Box width * number of blocks
        canvas.config(width=total_width, height=100)

        # Draw the Gantt chart
        x_start = 20
        y = 50
        box_width = 30

        for index, process in enumerate(self.scheduler.gantt_chart):
            if process == "Idle":
                color = "#CCCCCC"
            else:
                color = get_blue_gradient(self.scheduler.gantt_chart.index(process), len(self.scheduler.gantt_chart))

            canvas.create_rectangle(x_start, y - 20, x_start + box_width, y + 20, fill=color, outline="black")
            canvas.create_text(x_start + box_width // 2, y, text=process, font=("Arial", 10), fill="black")
            x_start += box_width

        # Draw the time labels on the X-axis
        x_start = 20
        for t in range(len(self.scheduler.gantt_chart) + 1):
            canvas.create_text(x_start, y + 30, text=str(t), font=("Arial", 10))
            x_start += box_width
