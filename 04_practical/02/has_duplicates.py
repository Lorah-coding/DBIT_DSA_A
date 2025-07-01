def has_duplicates(list):
    for a in range(len(list)):
        for b in range(a + 1, len(list)):
            if list[a] == list[b]:
                return True
    return False

print(has_duplicates([1, 8, 2, 3, 2, 6, 8]))  
print(has_duplicates([1, 2, 3, 4]))     
