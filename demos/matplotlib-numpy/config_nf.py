# Global variables

import math

# Input assumed variables here
# NF = 2 #dB
N_LF = 10**(-10)
k_DC = 1
kB = 1.381*(10**(-23))                                  # Boltzmann constant
#kB = 8.617*(10**(-5))                                  # Boltzmann constant
T = 300                                                 # K
Rs = 50                                                 # Ohms
Av_dB = 10                                              # dB
No_ED = 534.1083*10**(-9)                               # V**2/Hz
n = 1.5
Vt = 0.026
#Rin = 50
SNR_min = 12                                            # dB (for OOK, at 10^-3 BER)
BW = 0.01 #MHz

# Dependent variables, do not edit
#~ F = 10**(NF/10)                                      # Front-end amplifier noise factor
Nsrc = 4*kB*T*Rs                                        # Source-generated noise
GP = 10**(Av_dB/10)                                     # Front-end amplifier gain
GT = math.sqrt(GP)
BWdet = BW*(10**6)                                      # Envelope detector bandwidth

# Lower N_LF and No_ED will improve the sensitivity, making the graph approach the limit faster.