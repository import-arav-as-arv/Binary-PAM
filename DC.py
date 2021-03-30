import numpy as np              
import matplotlib.pyplot as plt #for visualization
from scipy import special
import math
import random
from math import e

#First, we define the Q-function with the help of scipy module
def QFunction(x):
    Q = 0.5*special.erfc(x/np.sqrt(2))
    return Q

#Given range of SNR values to be 0<10log(Eb/No)<=7
SNR1=np.arange(0,8,1) #SNR for simulation (dB)
SNR2=np.arange(0,7,0.1)#SNR (theoritical value) (in dB)
len1=len(SNR1)
len2=len(SNR2)
#for storing values of snr
SNR_l1=np.zeros(len1)
SNR_l2=np.zeros(len2)

#For storing the (sigma) ie. Std Deviation
sig2=np.zeros(len1)

#initializing prob of error values to zero
err_p1 = np.zeros(len1) #Prob of error for simulated result
err_p2 = np.zeros(len2) #Prob of error for theoritical result

N=10000 #No. of bits to be transmitted (Given in the question)

#Simulation of Prob. of error

for i in range(len1):
    Eb=2
    snr_n= e**((SNR1[i])*np.log(10)/10) #Computing in Linear metrics (not dB)
    SNR_l1[i]=snr_n
    sig2[i]=np.sqrt(Eb/SNR_l1[i])
    

    #Generating a binary sequence for transmission
    b_source=np.zeros(N)
    for j in range(N):
        b_source[j] = random.randint(0,1) #generates a random number between 0 and 1

    #A counter variable to keep a track of the error
    count=0

    #Adding a Gaussian noise and demodulating

    for j in range(N):
        if(b_source[j]==0):
            y=-np.sqrt(Eb) + np.random.normal(0, sig2[i])
        else:
            y = np.sqrt(Eb) + np.random.normal(0, sig2[i])

        #Predicting the correct output using Detector and a threshold value
        if (y<0):
            predicted_res=0
        else:
            predicted_res=1
        
        if(predicted_res!=b_source[j]):
            count+=1

        err_p1[i]=count/N
#simulation ends here

#Computing Theoritical values...

for i in range(len2):
    snr_n=e**((SNR2[i])*np.log(10)/10)
    # SNR_l2[i]=snr_n
    err_p2[i]=QFunction(np.sqrt(snr_n))

plt.figure("Output Window ECE-18009")
plt.title("Probability of error for Binary PAM")
plt.ylabel("Probability of Error ----->")
plt.xlabel("SNR/bit in dB ------>")
plt.plot(SNR2,err_p2,label='Theoretical Result') 
plt.plot(SNR1,err_p1,'o-',label='Simulated Result', color = 'Red')
plt.legend(ncol=2,frameon='True')
plt.grid()
plt.show()



