import numpy as np 


x = np.fromfunction(lambda i, j:j+i, (4,5), dtype=np.float16)

print(x)
