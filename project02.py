def maximize_grade(N, P, K):
    # Convert string to list for easier manipulation
    grades = list(N)
    length = len(grades)
    
    # Bubble sort with a maximum of K swaps
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if grades[j] > grades[j + 1]:
                grades[j], grades[j + 1] = grades[j + 1], grades[j]
                swapped = True
                K -= 1
                if K == 0:
                    break
        if not swapped or K == 0:
            break
    
    # Ensure the lexicographically smallest character is at index P
    sorted_str = ''.join(grades)
    return min(sorted_str[P-1], sorted_str)

# Sample Input
N = "abcdefg"
P = 3
K = 2

# Calculate and print the maximized grade
print("Maximized grade:", maximize_grade(N, P, K))
