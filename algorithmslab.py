def char_frequency(string):
    freq = {}
    for char in string:
        if char != " ":  # Exclude spaces
            freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("data structures and algorithms"))