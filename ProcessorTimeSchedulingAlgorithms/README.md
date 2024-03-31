# Processor Time Scheduling Algorithms

This folder contains Python scripts implementing two processor time scheduling algorithms: FCFS (First-Come, First-Served) and SJF (Shortest Job First).

## FCFS Algorithm (First-Come, First-Served)

The FCFS algorithm is one of the simplest scheduling algorithms where the process that arrives first is served first. This script simulates the FCFS algorithm by generating random arrival times and burst times for processes and calculates the waiting time, turnaround time and completion time for each process.

### How FCFS Works

1. A DataFrame with arrival times and burst times of processes is created and sorted based on arrival times.
2. Lists for turnaround times, waiting times, and completion times are initialized.
3. The completion time and waiting time for each process are calculated.
4. Results are displayed in a table.

### Usage

1. Run `FCFS_algorithm.py` to execute the FCFS algorithm.
2. The script generates random arrival times and burst times, simulates process scheduling using the FCFS algorithm and outputs the results to a text file named `FCFS_data.txt`.
3. The output includes the arrival time, burst time, completion time, turnaround time and waiting time for each process.

## SJF Algorithm (Shortest Job First)

This is the non-preemptive SJF algorithm. This script implements the SJF algorithm and calculates the waiting time, turnaround time and completion time for each process.

### How SJF Works

1. Processes are sorted based on arrival times.
2. The process with the shortest burst time among the ready processes is selected for execution.
3. Waiting time, turnaround time and completion time for each process are calculated.
4. Results are displayed in a table.

### Usage

1. Run `SJF_algorithm.py` to execute the SJF algorithm.
2. The script generates random arrival times and burst times, simulates process scheduling using the SJF algorithm and outputs the results to a text file named `SJF_data.txt`.
3. The output includes the arrival time, burst time, completion time, turnaround time, and waiting time for each process.

Author Natalia Polak
