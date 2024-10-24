def reverse_in_groups(lst, n):
    result = []
    for i in range(0, len(lst), n):
        group = []
        # Manually reverse the group of n elements
        for j in range(min(n, len(lst) - i)):
            group.insert(0, lst[i + j])
        result.extend(group)
    return result

# Example usage:
print(reverse_in_groups([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]
print(reverse_in_groups([1, 2, 3, 4, 5], 2))           # Output: [2, 1, 4, 3, 5]
print(reverse_in_groups([10, 20, 30, 40, 50, 60, 70], 4))  # Output: [40, 30, 20, 10, 70, 60, 50]
