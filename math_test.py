import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import matplotlib as mpl

# Test Array 1
arr1 = np.ones((4, 4))
arr1[2, 0] = 10

z = np.zeros((2, 2))

arr1[1:3, 1:3] = z

print(arr1)


# Test Array 2 
arr2 = np.identity(10)
print("=" * 30)
print(f"Identity matrix determinant: {np.linalg.det(arr2)}")
print(arr2)
print("-" * 25 + " part B:")

print(arr2 + 2)
print(f"Determinant with + 2: {np.linalg.det(arr2 + 2)}")


# Test Array 3 
print("=" * 30)
data_for_array_3 = np.full((10, 10), 6)
y_axis_labels = ['Test1','Test2','Test3','Test4','Test5','Test6','Test7','Test8','Test9','Test10']

arr3_df = pd.DataFrame(data_for_array_3, index=y_axis_labels)
print(arr3_df.describe())
print(arr3_df)


# Test DataFrame 
print("=" * 30)
df_data_implmt = np.zeros((5, 5))
arr3_df.iloc[4:9, 4:9] = df_data_implmt
print(arr3_df)