
import numpy as np



arr_4= np.arange(50 , 98 , 2).reshape(2 , 3 , 4)
print(arr_4)


# 12. Find the sum of each row of arr_4
print(f"Sum of each row: {np.sum(arr_4, axis=1)}")