# Created by Denise Soriano on 9/26/2019
# Last updated: 11/9/2023
# Compatible with Python 3.12.0

import matplotlib.pyplot as plt
import numpy as np
import os
from config_nf import *

NF = np.arange(0, 10, 0.5) #dB
F = 10**(NF/10)

# Calculate noise factor of ith amplifier
def Famp(i):
	
	F_amp = F
	
	if i > 1:
		for x in range(2, i+1):
			num = F - 1
			den = GT**(x-1)
			F_amp += num/den
		
	return F_amp

# Calculate effective noise factor of ith stage
def Fi(i):
	
	num = N_LF*(k_DC**2)*No_ED
	den = Nsrc*(GT**(2*i))
	F_i = 2*Famp(i) + num/den
	
	return F_i
	
# Calculate total effective noise factor
def Ftot(i):
	
	num = tmpden = 0
	
	for x in range(1, i+1):
		num += Fi(x)*((GT**i)**2)
		tmpden += GT**i
	den = (abs(tmpden))**2
		
	if den!=0:
		F_tot = num/den
	else:
		F_tot = None
	
	return F_tot

# Get sensitivity/minimum detectable signal level
def sens(x):
	
	Pn_in = -174 + 10*np.log10(BWdet) + 10*np.log10(Ftot(x))
	Pmds = Pn_in + SNR_min
		
	return Pmds
	
# Calculate everything and plot
def magic_plot(*stages):
	
	plt.figure(figsize=(7,7))

	no_of_stages = stages[0] if len(stages) > 0 else 5
	
	for stage in range(1, no_of_stages + 1):
		sens_list = sens(stage)
		plt.plot(NF, sens_list, label=stage)
		
	plt.xlabel('Noise Figure (dB)')
	plt.ylabel('Sensitivity (dBm)')
	plt.legend(title='Number of Stages', bbox_to_anchor=(0.85, 1.15), ncol=5, fancybox = True, shadow=True)

	# Automatically save png file to images folder
	try:
		path, dirs, files = next(os.walk("saved-images"))
		file_count = len(files)
		file_count_str = str(file_count)
		if len(file_count_str) == 1: filename = f'00{file_count_str}.png'
		elif len(file_count_str) == 2: filename = f'0{file_count_str}.png'
		else: filename = '%s.png' % (file_count_str)
		file_name = f"saved-images/{filename}"
		plt.savefig(file_name)
	except Exception as e:
		print(f"Error saving figure")
	
	plt.show()
	
if __name__ == "__main__":
	
	while True:
		try:
			stages = int(input("Define number of stages>>>: "))
			magic_plot(stages)
		except ValueError:
			print("Invalid input, exiting app")
			break
