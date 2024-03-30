import random
import pandas as pd
import numpy as np
from prettytable import PrettyTable

''' 
Jak działa algorytm FCFS?
1. Zostaje utworzona dwukolumnowa DataFrame, ktora zawiera informacje o czasach przyjścia i czasach wykonania procesów
2. DataFrame zostaje posortowana względem czasów przyjścia
3. Inicjalizuję listy na czasy:
 - turnaround_times - jest to różnica między czasem zakończenia procesu a jego czasem przyjścia.
 - waiting_times - jest to różnica między czasem turnaround, a czasem wykonywania danego procesu. 
 Oznacza, ile czasu proces musiał czekać na swoją kolej w kolejce oczekujących przed rozpoczęciem wykonania
 - completion_times - przechowuje czasy zakończenia dla poszczególnych procesów
 4. Zostaje obliczeny czas zakończenia i czas oczekiwania dla procesów
 5. Obliczenia czasu turnaround dla wszystkich procesów
 6. Wyświetlenie wyników w tabeli
'''

def data_generator():
    random.seed(50)
    num_processes = 20 #np.abs(np.random.randint(3, 12)) tyle będzie procesów do symulowania
    arrival_times = [random.randint(1, 20) for i in range(num_processes)]
    #np.round(np.abs(np.random.normal(5.5,4.5,  size=num_processes)), 3)
    # np.abs odpowiada za to, że wyniki są dodatnie, bo zwraca wartość bezwzględną
    # pierwsza wartość to średnia czasu przyjścia, druga to odchylenie standardowe czasu przyjścia w rozkładzie normalnym
    burst_times = [random.randint(1, 20) for i in range(num_processes)]
    #np.round(np.random.normal(5.5,4.5,  size=num_processes), 3)  # generuje losowe czasy wykonania procesów
    return arrival_times, burst_times


def FCFS_algorithm(arrival_times, burst_times):
    N = len(arrival_times)

    index = list(range(len(arrival_times)))
    # Sortujemy indeksy na podstawie czasu przyjścia
    index.sort(key=lambda i: arrival_times[i])

    # Aktualizujemy oryginalne listy zgodnie z posortowanymi indeksami
    arrival_times = [arrival_times[i] for i in index]
    burst_times = [burst_times[i] for i in index]

    waiting_times = [0] * N
    completion_times = [0] * N

    processes = pd.DataFrame({
        'Arrival Time': arrival_times,
        'Burst Time': burst_times
    })

    # dla pierwszego procesu:
    completion_times[0] = processes['Burst Time'].iloc[0] + processes['Arrival Time'].iloc[0]
    waiting_times[0] = 0

    # dla reszty procesów
    for i in range(1, N):
        arrival_i = processes['Arrival Time'].iloc[i]
        burst_i = processes['Burst Time'].iloc[i]

        # maksimum między czasem przyjścia danego procesu a czasem zakończenia poprzedniego procesu zwiększonego o czas wykonania bieżącego procesu
        completion_times[i] = max(arrival_i, completion_times[i-1]) + burst_i
        # różnica między czasem zakończenia a czasem przyjścia i czasem wykonania procesu
        waiting_times[i] = completion_times[i] - arrival_i - burst_i

    turnaround_times = np.round(np.array(completion_times) - np.array(processes['Arrival Time'].tolist()), 3)

    processes_sorted = processes.sort_values(by='Arrival Time')
    result_table = PrettyTable()
    result_table.field_names = ["Arrival Time", "Burst Time", "Completion Time", "Turnaround Time",
                                "Waiting Time"]

    for i in range(N):
        result_table.add_row([
            round(processes_sorted['Arrival Time'].iloc[i], 3),
            round(processes_sorted['Burst Time'].iloc[i], 3),
            round(completion_times[i], 3),
            round(turnaround_times[i], 3),
            round(waiting_times[i], 3)
        ])

    index_table = list(range(1, N + 1))

    table = pd.DataFrame({
        'Process ID': index_table,
        'Waiting Time': waiting_times,
        'Turnaround Time': turnaround_times,
        'Completion Time': completion_times
    })

    print("Results of FCFS algorithm:")
    print(result_table)

    return turnaround_times, waiting_times, table


def results(turnaround_times,waiting_times, table):
    average_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    print("Average Turnaround Time: " + str(round(average_turnaround_time, 3)) + "\n")
    average_waiting_time = sum(waiting_times) / len(waiting_times)
    print("Average Waiting Time: " + str(round(average_waiting_time, 3)) + "\n")

    table.to_csv(r'FCFS_data.txt', header=True, index=None, sep='\t', mode='a', float_format='%.3f')
    file = open("FCFS_data.txt", "a")
    file.write("Average Turnaround Time: " + str(average_turnaround_time) + "\n")
    file.write("Average Waiting Time: " + str(average_waiting_time) + "\n")
    file.close()


arrival_times, burst_times = data_generator()
print(f"Arrival times: {arrival_times}")
print(f"Burst times: {burst_times}")
turnaround_times, waiting_times, table = FCFS_algorithm(arrival_times, burst_times)
results(turnaround_times, waiting_times, table)
