import sys 
print(f"Python {sys.version}")

import numpy as np  
print(f"NumPy {np.__version__}")
a = np.array([1, 2, 3])
print(f"Вектор: {a}, скалярное произведение с самим собой: {np.dot(a, a)}")

import torch
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
 print(f"GPU: {torch.cuda.get_device_name(0)}")
 