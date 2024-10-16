import lec_3_my_module
import numpy as np 

h = 100 
alfa = 45 
betta = 35
g = lec_3_my_module.g
z = (g*h*(np.tan(betta)**2)/(2 *np.cos(alfa)**2 )*(1-np.tan(betta)* np.tan(alfa))) ** 0.5
print(z)

