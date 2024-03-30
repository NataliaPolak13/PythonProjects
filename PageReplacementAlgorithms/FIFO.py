import random
import numpy as np

def data_generator():
    random.seed(10)
    #num_pages = 50
    num_pages = np.abs(np.random.randint(5, 15)) # ilość stron
    page_numbers = np.abs(np.random.randint(1, 20, size=num_pages)) # losowe numery stron
    size = 4 # ile stron jest przechowywanych w danym czasie
    return page_numbers, num_pages, size

def FIFO_algorithm(pages, size):
    page_hits = 0 # licznik trafień gdy strona jest w pamięci
    page_faults = 0 # licznik błędów strony (gdy musi zostać załadowana do pamięci)
    queue = [] # przechowuje strony

    for page in pages:
        if page in queue:  # Sprawdzanie czy strona jest w pamięci podręcznej
            page_hits += 1
        else:
            if len(queue) == size:
                # Usuwanie najstarszej strony (pierwszej na liście)
                removed_page = queue.pop(0) # Usuwanie elementu o indeksie 0
                print(f'Removed page: {removed_page}')
            queue.append(page)  # Dodawanie nowej strony do końca kolejki
            page_faults += 1
        print(queue)

    file = open("FIFO_data.txt", "a")
    file.write(str(queue))
    file.write("Page Hits: " + str(page_hits)+ "\n")
    file.write("Page Faults: " + str(page_faults)+ "\n")
    file.close()

    return page_hits, page_faults


pages, num, size = data_generator()
page_hits, page_faults = FIFO_algorithm(pages, size)


print("Pages: " + str(pages))
print("Number of pages: " + str(num))
print("Page Hits: " + str(page_hits))
print("Page Faults: " + str(page_faults))