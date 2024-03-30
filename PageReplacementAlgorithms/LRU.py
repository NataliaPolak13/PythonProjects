import random
import numpy as np

def data_generator():
    random.seed(10)
    #num_pages = 50 ilość stron
    num_pages = np.abs(np.random.randint(5, 15)) # ilość stron, które wylosowano
    page_numbers = np.random.randint(1, 20, size=num_pages) # losowe numery stron
    capacity = 100 # ile stron jest przechowywanych w danym czasie
    return page_numbers, num_pages, capacity

def LRU_algorithm(pages, num, capacity):
    page_hit = 0
    page_fault = 0
    cache = {}  # Słownik przechowujący czas ostatniego użycia dla każdej strony
    time_index = 0  # Zmienna śledząca czas
    queue = []  # Kolejka do śledzenia aktualnej kolejności stron w pamięci podręcznej

    for i in range(num):
        if pages[i] in cache: # Sprawdzenie czy strona jest w pamięci
            page_hit += 1
            cache[pages[i]] = time_index  # Aktualizacja czasu ostatniego użycia
            queue.remove(pages[i]) # Usuwanie tej strony z kolejki
        else:
            page_fault += 1
            if len(cache) >= capacity: # Sprawdzenie czy pamięć podręczna jest już pełna
                # Znajdujemy stronę o najstarszym czasie ostatniego użycia
                # klucz to strony, wartości to użycie (czas)
                # szukamy najmniejszej wartości
                page_to_del = min(cache, key=cache.get) # key -> wskazuje na funkcje, cache.get -> porównanie wartości dla klucza
                del cache[page_to_del]
                queue.remove(page_to_del)
            cache[pages[i]] = time_index  # Dodawanie nowej strony do pamięci podręcznej
        queue.append(pages[i]) # Dodawanie strony do kolejki
        time_index += 1
        print(f'Queue after iteration {i + 1}: {queue}')

    file = open("LRU_data.txt", "a")
    file.write(str(queue))
    file.write("Page Hits: " + str(page_hit) + "\n")
    file.write("Page Faults: " + str(page_fault))
    file.write("\n")
    file.close()

    return page_hit, page_fault


pages, num, size = data_generator()
page_hit, page_fault = LRU_algorithm(pages, num, size)

print("Pages: " + str(pages))
print("Number of pages: " + str(num))
print("Page Hits: " + str(page_hit))
print("Page Faults: " + str(page_fault))