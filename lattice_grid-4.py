#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

PI = 3.1415926535897
n_cell = 30
n_cell_x = 300000
n_cell_y = 300
res = 100
image_width=400
image_length=400
n_sample = 100
interval = 1.0/n_sample
x_c = np.linspace(0,1,n_sample+1)
grid_x = np.linspace(0,1,n_sample+1)
grid_y = np.linspace(0,1,n_sample+1)
grid_x[0]=n_cell_x**2
grid_x[n_sample] = n_cell_x**2
grid_y[0]=n_cell_y**2
grid_y[n_sample] = n_cell_y**2
for i in range(1,n_sample):
		x_1 = np.sin(n_cell_x*PI*i*interval)
		y_1 = np.sin(n_cell_y*PI*i*interval)
		xy_2 = np.sin(PI*i*interval)
		grid_x[i]= (x_1/xy_2)**2
		grid_y[i]= (y_1/xy_2)**2
#		print x_1, x_2
#		if x_2 != 0:
#			grid[i]= (x_1/x_2)**2
#		elif x_2 == 0:
#			grid[i] = n_cell**2
image_data = np.ones((image_width, image_length))


for i in range(image_width):
	for j in range(image_length):
		x_pos_low,x_pos_dec = divmod((i-200.0)/res,1)
		y_pos_low,y_pos_dec = divmod((j-200.0)/res,1)
		x_low,x_frac = divmod(x_pos_dec*n_sample,1)
		y_low,y_frac = divmod(y_pos_dec*n_sample,1)
		x_high = x_low +1
		y_high = y_low +1
		latt_x = (grid_x[x_low]*(1-x_frac)+grid_x[x_high]*x_frac)
		latt_y = (grid_y[y_low]*(1-y_frac)+grid_y[y_high]*y_frac)
		image_data[i,j] = latt_x*latt_y
"""
		numerator_1=np.sin(n_cell*PI*(i-200)/res)
		dominator_1=np.sin(PI*(i-200)/res)
		numerator_2=np.sin(n_cell*PI*(j-200)/res)
                dominator_2=np.sin(PI*(j-200)/res)

		if dominator_1 != 0 and dominator_2 != 0 :
			image_data[i,j] = (numerator_1*numerator_2/(dominator_1*dominator_2))**2
		elif dominator_1 == 0 and dominator_2 !=0:
			image_data[i,j] = (n_cell*numerator_2/dominator_2)**2

		elif dominator_1 != 0 and dominator_2 ==0:
                        image_data[i,j] = (n_cell*numerator_1/dominator_1)**2

		elif dominator_1 == 0 and dominator_2 ==0:
                        image_data[i,j] = n_cell**4
"""


#		image_data[i,j] = (np.sin(n_cell*PI*(i-200)/res)*np.sin(n_cell*PI*(j-200)/res)/(np.sin(PI*(i-200)/res)*np.sin(PI*(j-200)/res)))**2

#plt.plot(x_c,grid)
#plt.show()
plt.axis("off")
plt.imshow(image_data, cmap = plt.get_cmap('gray'))
plt.savefig("artificial_fig.png")
plt.show()




