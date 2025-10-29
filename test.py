import numpy as np
import matplotlib.pyplot as plt


d_meas_matrix = np.load('.\Sim_output_data\d_meas_matrix.npy')
print(d_meas_matrix)
print("Shape of d_meas_matrix:", d_meas_matrix.shape)

output_data_all_mn_locations = np.load('.\Sim_output_data\output_data_all_mn_locations.npy',allow_pickle=True)
print(output_data_all_mn_locations)
print("Shape of output_data_all_mn_locations:", output_data_all_mn_locations.shape)

'''
rangingfaultall = np.load('.\Sim_output_data\rangingfault_all.npy',allow_pickle=True)
print(rangingfaultall)
print("Shape of rangingfault_all:", rangingfaultall.shape)
'''

plt.figure()
plt.plot(d_meas_matrix[0,:], label = 'd_meas_matrix[0,:]')
plt.show()
