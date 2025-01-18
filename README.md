# Priority Scheduling Simulator with GUI

## Overview

The **Priority Scheduling Simulator** is a Python-based desktop application that demonstrates how processes are scheduled using the Priority Scheduling algorithm. It supports both **Preemptive** and **Non-Preemptive** modes and provides an intuitive user interface for adding processes, running simulations, and visualizing results.

## Features

- Input fields for specifying process data: Arrival Time, Burst Time, and Priority.
- **Modes:**
  - Preemptive Scheduling: Higher-priority processes can preempt running processes.
  - Non-Preemptive Scheduling: Processes complete execution once started.
- Visualization of scheduling results:
  - Tabular results with Waiting Time, Turnaround Time, Response Time for each process.
  - Gantt Chart for a timeline view of process execution.
- User-friendly and responsive GUI with vibrant, random colors to differentiate processes.

## How It Works

1. **Input Process Data:**
   - Enter `Arrival Time`, `Burst Time`, and `Priority` for each process.
   - Click **Add Process** to add the process to the scheduling queue.

2. **Choose Scheduling Mode:**
   - Select **Preemptive** or **Non-Preemptive** mode using the toggle buttons.

3. **Run Simulation:**
   - Click **Simulate** to compute and display results.

4. **View Results:**
   - A table displays metrics for each process: Waiting Time, Turnaround Time, Response Time.
   - The Gantt Chart visualizes the scheduling timeline with colorful blocks representing processes.

5. **Gantt Chart Details:**
   - Each process is represented with a unique color.
   - Idle times (if any) are shown in gray.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/priority-scheduling-simulator.git
