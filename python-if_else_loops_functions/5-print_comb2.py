#!/usr/bin/python3
numbers = [str(i).zfill(2) for i in range(0, 100)]
result = ', '.join(numbers)
print(result)
