**Overview**
This repository contains my implementation and analysis of two Quicksort algorithms for my graduate level data structures assignment. I implemented a deterministic version of Quicksort that always selects the first element as the pivot and a randomized version that selects the pivot uniformly at random. The goal of this project was to compare their performance on different input types and explain how pivot selection affects efficiency and scalability.

**Files Included**
  quicksort_analysis.py
  Contains the complete Python implementation of both deterministic and randomized Quicksort algorithms along with the experiment driver used to measure performance.

**How to Run the Code**
Install Python 3 on your system.
Clone the repository to your computer using the green Code button on GitHub.
Open a terminal or command prompt inside the project folder.
Run the program using: python3 quicksort_analysis.py

The script will run both Quicksort algorithms on multiple input sizes and data distributions and will print average runtime results in a formatted table.

**Summary of Findings**
The deterministic Quicksort works well on random data but performs very poorly on sorted or reverse-sorted inputs because the fixed pivot selection produces extremely unbalanced partitions.
The randomized Quicksort consistently performs in the expected order of n log n time across all input types because random pivot selection avoids systematic worst-case behavior.
The experiments clearly showed how even a small design decision like pivot choice can significantly impact algorithmic performance and reliability.
