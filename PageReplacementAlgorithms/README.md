# Page Replacement Algorithms

This folder contains Python scripts implementing two popular page replacement algorithms: FIFO (First In, First Out) and LRU (Least Recently Used).

## FIFO Algorithm

The FIFO (First In, First Out) algorithm is one of the simplest page replacement algorithms. It operates on the principle of replacing the oldest page in memory. When a page needs to be replaced, the one that has been in memory the longest is evicted. This script simulates the FIFO algorithm by generating random page numbers and tracking page hits and faults.

### How FIFO Works

1. The algorithm maintains a queue to keep track of the order in which pages are loaded into memory.
2. When a new page needs to be loaded into memory, the algorithm removes the page at the front of the queue (the oldest page) if the memory is full.
3. The new page is then added to the end of the queue.
4. If the page to be loaded is already in memory, it is considered a "page hit." Otherwise, it is a "page fault."

### Usage

1. Run `FIFO_algorithm.py` to execute the FIFO algorithm.
2. The script will generate random page numbers, simulate page replacements using the FIFO algorithm, and output the results to a text file named `FIFO_data.txt`.
3. The output includes the pages, number of pages, page hits, and page faults.

## LRU Algorithm

The LRU (Least Recently Used) algorithm replaces the least recently used page when a new page needs to be brought into memory. It keeps track of the order in which pages are accessed and removes the page that has not been used for the longest time. This script implements the LRU algorithm and provides insights into its performance.

### How LRU Works

1. The algorithm maintains a data structure, such as a dictionary, to keep track of the time of the last access for each page.
2. When a new page needs to be loaded into memory, the algorithm evicts the page that was least recently used.
3. If a page is accessed again, its entry in the data structure is updated.
4. If the page to be loaded is already in memory, it is considered a "page hit." Otherwise, it is a "page fault."

### Usage

1. Run `LRU_algorithm.py` to execute the LRU algorithm.
2. The script generates random page numbers, simulates page replacements using the LRU algorithm, and outputs the results to a text file named `LRU_data.txt`.
3. The output includes the pages, number of pages, page hits, and page faults.

Author Natalia Polak
