def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

print(linear_search([10, 20, 30, 40], 30)) 
print(linear_search([5, 6, 7], 10))         
