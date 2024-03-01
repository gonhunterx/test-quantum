for i in range(10):
    print(i)

for num in range(10):
    if num == 5:
        continue 
    print(num)
    
print(min(88, 22))


nums = list(range(10)) + list(range(5))
print(nums)
print(set(nums))

import numpy as np 

grades = np.array([[87, 96, 70], [100, 87, 90], [94, 77, 90], [100, 81, 82]])
print(grades[0:2])

# list of row indices
print(grades[[1, 3]])