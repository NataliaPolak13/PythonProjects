import random
import pandas as pd
from prettytable import PrettyTable

def data_generator():
    random.seed(50)
    num_processes = 4
    arrival_times = [0,2,3,5]#[random.randint(1, 20) for i in range(num_processes)]
    burst_times = [5,4,2,6]#[random.randint(1, 20) for i in range(num_processes)]
    return arrival_times, burst_times


def SJF_algorithm(arrival_times, burst_times):
    N = len(arrival_times)

    index_table = list(range(1, N + 1))

    current_time = 0
    waiting_times = [0] * N
    turnaround_times = [0] * N
    completion_times = [0] * N

    processes = list(zip(index_table, arrival_times, burst_times)) # łączę trzy listy w jedną krotkę

    while any(burst_time > 0 for i, j, burst_time in processes): # Pętla wykonuje się do kiedy są jeszcze dostępne procesy
        ''' Tworzę listę gotowych procesów ->
         te których czas przyjścia jest mniejszy lub równy aktualnemu czasowi wykonania 
         i których czas trwania jest większy od zera'''


        ready_processes = [process for process in processes if process[1] <= current_time and process[2] > 0]

        if not ready_processes: # Jeśli nie ma gotowych procesów -> zwiększam czas oczekiwania +1
            current_time += 1
            continue

        next_process = min(ready_processes, key=lambda x: x[2]) # Wybieram proces o najkrótszym czasie trwania

        process_id, arrival_time, burst_time = next_process

        waiting_times[process_id - 1] = max(0, current_time - arrival_time) # Obliczam czas oczekiwania dla danego procesu
        turnaround_times[process_id - 1] = waiting_times[process_id - 1] + burst_time # Obliczam czas całkowity dla danego procesu
        current_time += burst_time # aktualizuje aktualny czas wykonania
        completion_times[process_id - 1] = current_time # Zapisuje czas zakończenia wykonania dla danego procesu

        updated_processes = []
        for proc_id, arr_time, burst_time in processes: # iteruje przez procesy
            # jeśli to jest proces, który właśnie został wykonany, to zaktualizuje jego czas trwania na 0, ponieważ został zakończony
            if proc_id == process_id:
                updated_processes.append((proc_id, arr_time, max(0, burst_time - burst_time)))
            else: # w innym wypadku zachowuje istniejące informacje o procesie
                updated_processes.append((proc_id, arr_time, burst_time))

        processes = updated_processes

    average_waiting_time = sum(waiting_times) / N
    average_turnaround_time = sum(turnaround_times) / N

    print("\n" + f"Average Waiting Time: {average_waiting_time:}")
    print(f"Average Turnaround Time: {average_turnaround_time:}")

    table = pd.DataFrame({
        'Process ID': index_table,
        'Arrival Time': arrival_times,
        'Waiting Time': waiting_times,
        'Turnaround Time': turnaround_times,
        'Completion Time': completion_times
    })
    #table.set_index('Process ID', inplace=True)

    print("\n"+"Result Table:")
    result_table = PrettyTable()
    result_table.field_names = ["Completion Time", "Turnaround Time", "Waiting Time"]

    for i in range(N):
        result_table.add_row([
            (completion_times[i]),
            (turnaround_times[i]),
            (waiting_times[i])
        ])
    print(result_table)

    return turnaround_times, waiting_times, table


def results(turnaround_times, waiting_times, table):
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    print("Average Turnaround Time: " + str(average_turnaround_time) + "\n")
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    print("Average Waiting Time: " + str(average_waiting_time) + "\n")

    table.to_csv(r'SJF_data.txt', header=True, index=None, sep='\t', mode='a', float_format='%.3f')
    file = open("SJF_data.txt", "a")
    file.write("Average Turnaround Time: " + str(average_turnaround_time) + "\n")
    file.write("Average Waiting Time: " + str(average_waiting_time) + "\n")
    file.close()


arrival_times, burst_times = data_generator()
print(f"Arrival times: {arrival_times}")
print(f"Burst times: {burst_times}")
turnaround_times, waiting_times, table = SJF_algorithm(arrival_times, burst_times)
results(turnaround_times, waiting_times, table)
