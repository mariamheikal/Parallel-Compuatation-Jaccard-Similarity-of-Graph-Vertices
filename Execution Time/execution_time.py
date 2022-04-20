
import matplotlib.pyplot as plt
import numpy as np
  
  

x_dataset_size=[4.36,8.62,9.87,21.0]
#y_exec_time=[133.773997,742.177010,632.952988,3024.295092]#756.5,774.6,3807.3]
#y_kernel0_exec_time=[20.376001,80.875002,58.674999,264.667004]#62.694997]#,85.193001,87.337002]

y_cpu=[131.2,643.9,630.1,2788.6]
y_k0=[19.0,88.5,60.5,277.8]
y_k1=[13.3,50.9,51.7,576.2]
plt.plot(x_dataset_size, y_cpu, color = 'red',
         linestyle = 'solid', marker = 'o',
         markerfacecolor = 'black', markersize = 5,label='CPU')
plt.plot(x_dataset_size, y_k0, color = 'blue',
         linestyle = 'solid', marker = 'o',
         markerfacecolor = 'black', markersize = 5,label='Kernel 0')
plt.plot(x_dataset_size, y_k1, color = 'green',
         linestyle = 'solid', marker = 'o',
         markerfacecolor = 'black', markersize = 5,label='Kernel 1')
plt.legend()
plt.xlabel("Dataset Size (MB)")
plt.ylabel("Execution Time (ms)")
plt.title("Execution Time versus Dataset Size")
plt.show()  
plt.figure()
