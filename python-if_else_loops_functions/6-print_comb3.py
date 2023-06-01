#!/usr/bin/python3
combinations = [f'{i}{j}' for i in range(10) for j in range(i + 1, 10)]
result = '. '.join(combinations)
print(result)
