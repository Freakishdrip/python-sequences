#!/usr/bin/env python3
fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def print_fibonacci(length):
    arr = []
    i = 0
    print(f"{fibonacci_list[:length]}")
    # while(i <= length):
    #   arr.append(fibonacci_list[i])
    #   # print(fibonacci_list[i])
    #   i += 1
    # print(arr)
print_fibonacci(0)