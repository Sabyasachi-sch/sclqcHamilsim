import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, ticker
import matplotlib.colors

import matplotlib.colors as mcolors

from matplotlib.colors import LogNorm

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.linewidth'] = 1
plt.rcParams["axes.edgecolor"] = "black"

delt = 0.001
time_array = [delt]*(np.array(np.unique(np.round(np.logspace(0, 3, 50)).astype(int))))

with open('frb_norm_qno3.txt') as f:
    lines1 = f.readlines()

    
Frb_norm3=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm3.append(float(np.real(float(real_part))))

############################################################################
with open('frb_norm_qno4.txt') as f:
    lines1 = f.readlines()

    
Frb_norm4=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm4.append(float(np.real(float(real_part))))

############################################################################
with open('frb_norm_qno5.txt') as f:
    lines1 = f.readlines()

    
Frb_norm5=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm5.append(float(np.real(float(real_part))))

############################################################################
with open('frb_norm_qno6.txt') as f:
    lines1 = f.readlines()

    
Frb_norm6=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm6.append(float(np.real(float(real_part))))

############################################################################
with open('frb_norm_qno7.txt') as f:
    lines1 = f.readlines()

    
Frb_norm7=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm7.append(float(np.real(float(real_part))))

############################################################################
with open('frb_norm_qno8.txt') as f:
    lines1 = f.readlines()

    
Frb_norm8=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm8.append(float(np.real(float(real_part))))

############################################################################
with open('frb_norm_qno9.txt') as f:
    lines1 = f.readlines()

    
Frb_norm9=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm9.append(float(np.real(float(real_part))))
    
############################################################################
with open('frb_norm_qno10.txt') as f:
    lines1 = f.readlines()

    
Frb_norm10=[]

for line in lines1:
    S = line.split()
    # Extract the real part of the complex number
    real_part = S[0].strip("()").split("+")[0]  # Assuming the format '(real+imaginaryj)'
    Frb_norm10.append(float(np.real(float(real_part))))
    
############################################################################
with open('frb_norm_qno11.txt') as f:
    lines1 = f.readlines()

    
Frb_norm11=[]

for line in lines1:
    S = line.split()
    
    Frb_norm11.append(float(S[0]))
    
############################################################################
with open('frb_norm_qno12.txt') as f:
    lines1 = f.readlines()

    
Frb_norm12=[]

for line in lines1:
    S = line.split()
    
    Frb_norm12.append(float(S[0]))
    

############################################################################
with open('frb_norm_qno13.txt') as f:
    lines1 = f.readlines()

    
Frb_norm13=[]

for line in lines1:
    S = line.split()
    
    Frb_norm13.append(float(S[0]))

############################################################################
with open('frb_norm_qno14.txt') as f:
    lines1 = f.readlines()

    
Frb_norm14=[]

for line in lines1:
    S = line.split()
    
    Frb_norm14.append(float(S[0]))

############################################################################
with open('frb_norm_qno15.txt') as f:
    lines1 = f.readlines()

    
Frb_norm15=[]

for line in lines1:
    S = line.split()
    
    Frb_norm15.append(float(S[0]))

############################################################################
with open('frb_norm_qno16.txt') as f:
    lines1 = f.readlines()

    
Frb_norm16=[]

for line in lines1:
    S = line.split()
    
    Frb_norm16.append(float(S[0]))

############################################################################
with open('frb_norm_qno17.txt') as f:
    lines1 = f.readlines()

    
Frb_norm17=[]

for line in lines1:
    S = line.split()
    
    Frb_norm17.append(float(S[0]))

############################################################################
with open('frb_norm_qno18.txt') as f:
    lines1 = f.readlines()

    
Frb_norm18=[]

for line in lines1:
    S = line.split()
    
    Frb_norm18.append(float(S[0]))

############################################################################


Qubit_no = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

Error_array = np.array([Frb_norm3,Frb_norm4,Frb_norm5,Frb_norm6,Frb_norm7,Frb_norm8,Frb_norm9,Frb_norm10,Frb_norm11,Frb_norm12,Frb_norm13,Frb_norm14,Frb_norm15,Frb_norm16,Frb_norm17,Frb_norm18])

#############################################################################

fig = plt.figure(figsize=(10,8))

label_arr = ['n=3', 'n=4', 'n=5', 'n=6', 'n=7', 'n=8', 'n=9', 'n=10', 'n=11','n=12', 'n=13', 'n=14', 'n=15', 'n=16', 'n=17', 'n=18']

for i in range(len(label_arr)):
    plt.loglog(time_array,Error_array[i],lw="3",label= label_arr[i])


plt.xlabel(r"Time in unit of $\hbar$",fontsize=23)
plt.ylabel("Error",fontsize=23)

plt.xticks(fontsize=18)
plt.yticks(fontsize=18)


plt.legend(loc="lower left",fontsize=12)

plt.ylim(1.e-15,2.e-11)

plt.grid(color='grey', which='both', axis='both', alpha=0.7)

fig.savefig('ising.png', dpi=500)

plt.show()

tick_list = [2e-15, 6e-15, 2e-14, 6e-14, 2e-13, 7e-13, 2e-12, 7e-12, 1.2e-11]

tick_list = sorted(set(tick_list))


cmap = cm.Purples
norm = mcolors.BoundaryNorm(boundaries=tick_list, ncolors=cmap.N, extend='both')


fig, ax = plt.subplots(figsize=(10, 8))  
cax = ax.contourf(time_array, Qubit_no, Error_array, levels=tick_list, norm=norm, cmap=cmap, extend='neither') 
ax.set_xscale("log")
ax.set_yticks(Qubit_no)

cb = fig.colorbar(cax, ticks=tick_list, extend='neither')  
cb.set_ticklabels([f"{tick:.1e}" for tick in tick_list])  
cb.ax.set_title("Error", fontsize=18, pad=10)


tick_font_size = 18
cb.ax.tick_params(labelsize=tick_font_size)


ax.set_xlabel(r"Time in unit of $\hbar$", fontsize=25)
ax.set_ylabel("Qubit", fontsize=25)


ax.tick_params(axis='both', which='major', labelsize=20, length=10, width=2, colors='black', direction='out')
ax.tick_params(axis='both', which='minor', labelsize=1, length=0.5, width=0.5, colors='black', direction='out')


ax.spines['right'].set_linewidth(2.5)  
ax.spines['top'].set_linewidth(2.5)    
ax.spines['bottom'].set_linewidth(2.5)
ax.spines['left'].set_linewidth(2.5) 

ax.text(.01, 1.06, '(a)',color="black", fontsize=25, ha='left', va='top', transform=plt.gca().transAxes)

fig.savefig('ISING_surf.png', dpi=300)
plt.show()