import matplotlib.pyplot as plt

import os

# Set the working directory to the path that contains 'Heisenberg' folder
os.chdir('C:/Users/User/Work_space/python_rohit/hamil_sim/All_plot_code_APL/Noise')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.linewidth'] = 1
plt.rcParams["axes.edgecolor"] = "black"

##################### 4qubit/down_ip   #############################
with open('Heisenberg/4qubit/down_ip/lowlow.txt') as f:
    lines1 = f.readlines()

time=[]    
lowlow_4=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowlow_4.append(float(S[1]))
    

with open('Heisenberg/4qubit/down_ip/lowhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
lowhigh_4=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowhigh_4.append(float(S[1]))
    

with open('Heisenberg/4qubit/down_ip/highlow.txt') as f:
    lines1 = f.readlines()

time=[]    
highlow_4=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highlow_4.append(float(S[1]))
    

with open('Heisenberg/4qubit/down_ip/highhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
highhigh_4=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highhigh_4.append(float(S[1]))
    

with open('Heisenberg/4qubit/down_ip/midmid.txt') as f:
    lines1 = f.readlines()

time=[]    
midmid_4=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    midmid_4.append(float(S[1]))
    
#####################################################

##################### 6qubit/down_ip   #############################
with open('Heisenberg/6qubit/down_ip/lowlow.txt') as f:
    lines1 = f.readlines()

time=[]    
lowlow_6=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowlow_6.append(float(S[1]))
    

with open('Heisenberg/6qubit/down_ip/lowhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
lowhigh_6=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowhigh_6.append(float(S[1]))
    

with open('Heisenberg/6qubit/down_ip/highlow.txt') as f:
    lines1 = f.readlines()

time=[]    
highlow_6=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highlow_6.append(float(S[1]))
    

with open('Heisenberg/6qubit/down_ip/highhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
highhigh_6=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highhigh_6.append(float(S[1]))
    

with open('Heisenberg/6qubit/down_ip/midmid.txt') as f:
    lines1 = f.readlines()

time=[]    
midmid_6=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    midmid_6.append(float(S[1]))
    
#####################################################

##################### 8qubit/down_ip   #############################
with open('Heisenberg/8qubit/down_ip/lowlow.txt') as f:
    lines1 = f.readlines()

time=[]    
lowlow_8=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowlow_8.append(float(S[1]))
    

with open('Heisenberg/8qubit/down_ip/lowhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
lowhigh_8=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowhigh_8.append(float(S[1]))
    

with open('Heisenberg/8qubit/down_ip/highlow.txt') as f:
    lines1 = f.readlines()

time=[]    
highlow_8=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highlow_8.append(float(S[1]))
    

with open('Heisenberg/8qubit/down_ip/highhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
highhigh_8=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highhigh_8.append(float(S[1]))
    

with open('Heisenberg/8qubit/down_ip/midmid.txt') as f:
    lines1 = f.readlines()

time=[]    
midmid_8=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    midmid_8.append(float(S[1]))
    
#####################################################

##################### 4qubit/all_1_ip   #############################
with open('Heisenberg/4qubit/all_1_ip/lowlow.txt') as f:
    lines1 = f.readlines()

time=[]    
lowlow_4up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowlow_4up.append(float(S[1]))
    

with open('Heisenberg/4qubit/all_1_ip/lowhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
lowhigh_4up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowhigh_4up.append(float(S[1]))
    

with open('Heisenberg/4qubit/all_1_ip/highlow.txt') as f:
    lines1 = f.readlines()

time=[]    
highlow_4up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highlow_4up.append(float(S[1]))
    

with open('Heisenberg/4qubit/all_1_ip/highhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
highhigh_4up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highhigh_4up.append(float(S[1]))
    

with open('Heisenberg/4qubit/all_1_ip/midmid.txt') as f:
    lines1 = f.readlines()

time=[]    
midmid_4up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    midmid_4up.append(float(S[1]))
    
#####################################################

##################### 6qubit/all_1_ip   #############################
with open('Heisenberg/6qubit/all_1_ip/lowlow.txt') as f:
    lines1 = f.readlines()

time=[]    
lowlow_6up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowlow_6up.append(float(S[1]))
    

with open('Heisenberg/6qubit/all_1_ip/lowhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
lowhigh_6up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowhigh_6up.append(float(S[1]))
    

with open('Heisenberg/6qubit/all_1_ip/highlow.txt') as f:
    lines1 = f.readlines()

time=[]    
highlow_6up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highlow_6up.append(float(S[1]))
    

with open('Heisenberg/6qubit/all_1_ip/highhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
highhigh_6up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highhigh_6up.append(float(S[1]))
    

with open('Heisenberg/6qubit/all_1_ip/midmid.txt') as f:
    lines1 = f.readlines()

time=[]    
midmid_6up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    midmid_6up.append(float(S[1]))
    
#####################################################

##################### 8qubit/all_1_ip   #############################
with open('Heisenberg/8qubit/all_1_ip/lowlow.txt') as f:
    lines1 = f.readlines()

time=[]    
lowlow_8up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowlow_8up.append(float(S[1]))
    

with open('Heisenberg/8qubit/all_1_ip/lowhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
lowhigh_8up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    lowhigh_8up.append(float(S[1]))
    

with open('Heisenberg/8qubit/all_1_ip/highlow.txt') as f:
    lines1 = f.readlines()

time=[]    
highlow_8up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highlow_8up.append(float(S[1]))
    

with open('Heisenberg/8qubit/all_1_ip/highhigh.txt') as f:
    lines1 = f.readlines()

time=[]    
highhigh_8up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    highhigh_8up.append(float(S[1]))
    

with open('Heisenberg/8qubit/all_1_ip/midmid.txt') as f:
    lines1 = f.readlines()

time=[]    
midmid_8up=[]

for line in lines1:
    S = line.split()
    time.append(float(S[0]))
    midmid_8up.append(float(S[1]))
    
#####################################################

fig, axs = plt.subplots(2, 3, figsize=(15, 10), gridspec_kw={'height_ratios': [1, 1]}, sharex='col', sharey='row')

# Plotting the data

axs[0, 0].plot(time,lowlow_4,lw="3",color="#3048F7",linestyle='-',label=r'Low Gate & Low Idle Noise',alpha=0.95)
axs[0, 0].plot(time,lowhigh_4,lw="3",color="#FF8F00",linestyle='--',label=r'Low Gate & High Idle Noise',alpha=0.85)
axs[0, 0].plot(time,highlow_4,lw="3",color="#AE00FF",linestyle=':',label=r'High Gate & Low Idle Noise',alpha=0.75)
axs[0, 0].plot(time,highhigh_4,lw="3",color="#FF2D2D",linestyle='-.',label=r'High Gate & High Idle Noise',alpha=0.65)
axs[0, 0].plot(time,midmid_4,lw="3",color="#486F3D",linestyle=(0, (3, 1, 1, 1)), label=r'Medium Gate & Idle Noise',alpha=0.55)

axs[0, 1].plot(time,lowlow_6,lw="3",color="#3048F7",linestyle='-',label=r'Low Gate & Low Idle Noise',alpha=0.95)
axs[0, 1].plot(time,lowhigh_6,lw="3",color="#FF8F00",linestyle='--',label=r'Low Gate & High Idle Noise',alpha=0.85)
axs[0, 1].plot(time,highlow_6,lw="3",color="#AE00FF",linestyle=':',label=r'High Gate & Low Idle Noise',alpha=0.75)
axs[0, 1].plot(time,highhigh_6,lw="3",color="#FF2D2D",linestyle='-.',label=r'High Gate & High Idle Noise',alpha=0.65)
axs[0, 1].plot(time,midmid_6,lw="3",color="#486F3D",linestyle=(0, (3, 1, 1, 1)), label=r'Medium Gate & Idle Noise',alpha=0.55)

axs[0, 2].plot(time,lowlow_8,lw="3",color="#3048F7",linestyle='-',label=r'Low Gate & Low Idle Noise',alpha=0.95)
axs[0, 2].plot(time,lowhigh_8,lw="3",color="#FF8F00",linestyle='--',label=r'Low Gate & High Idle Noise',alpha=0.85)
axs[0, 2].plot(time,highlow_8,lw="3",color="#AE00FF",linestyle=':',label=r'High Gate & Low Idle Noise',alpha=0.75)
axs[0, 2].plot(time,highhigh_8,lw="3",color="#FF2D2D",linestyle='-.',label=r'High Gate & High Idle Noise',alpha=0.65)
axs[0, 2].plot(time,midmid_8,lw="3",color="#486F3D",linestyle=(0, (3, 1, 1, 1)), label=r'Medium Gate & Idle Noise',alpha=0.55)

axs[1, 0].plot(time,lowlow_4up,lw="3",color="#3048F7",linestyle='-',label=r'Low Gate & Low Idle Noise',alpha=0.95)
axs[1, 0].plot(time,lowhigh_4up,lw="3",color="#FF8F00",linestyle='--',label=r'Low Gate & High Idle Noise',alpha=0.85)
axs[1, 0].plot(time,highlow_4up,lw="3",color="#AE00FF",linestyle=':',label=r'High Gate & Low Idle Noise',alpha=0.75)
axs[1, 0].plot(time,highhigh_4up,lw="3",color="#FF2D2D",linestyle='-.',label=r'High Gate & High Idle Noise',alpha=0.65)
axs[1, 0].plot(time,midmid_4up,lw="3",color="#486F3D",linestyle=(0, (3, 1, 1, 1)), label=r'Medium Gate & Idle Noise',alpha=0.55)

axs[1, 1].plot(time,lowlow_6up,lw="3",color="#3048F7",linestyle='-',label=r'Low Gate & Low Idle Noise',alpha=0.95)
axs[1, 1].plot(time,lowhigh_6up,lw="3",color="#FF8F00",linestyle='--',label=r'Low Gate & High Idle Noise',alpha=0.85)
axs[1, 1].plot(time,highlow_6up,lw="3",color="#AE00FF",linestyle=':',label=r'High Gate & Low Idle Noise',alpha=0.75)
axs[1, 1].plot(time,highhigh_6up,lw="3",color="#FF2D2D",linestyle='-.',label=r'High Gate & High Idle Noise',alpha=0.65)
axs[1, 1].plot(time,midmid_6up,lw="3",color="#486F3D",linestyle=(0, (3, 1, 1, 1)), label=r'Medium Gate & Idle Noise',alpha=0.55)

axs[1, 2].plot(time,lowlow_8up,lw="3",color="#3048F7",linestyle='-',label=r'Low Gate & Low Idle Noise',alpha=0.95)
axs[1, 2].plot(time,lowhigh_8up,lw="3",color="#FF8F00",linestyle='--',label=r'Low Gate & High Idle Noise',alpha=0.85)
axs[1, 2].plot(time,highlow_8up,lw="3",color="#AE00FF",linestyle=':',label=r'High Gate & Low Idle Noise',alpha=0.75)
axs[1, 2].plot(time,highhigh_8up,lw="3",color="#FF2D2D",linestyle='-.',label=r'High Gate & High Idle Noise',alpha=0.65)
axs[1, 2].plot(time,midmid_8up,lw="3",color="#486F3D",linestyle=(0, (3, 1, 1, 1)), label=r'Medium Gate & Idle Noise',alpha=0.55)


for ax in [axs[0, 0],axs[0, 1],axs[0, 2],axs[1, 0],axs[1, 1],axs[1, 2]]:
    ax.set_xscale('log')
    
    ax.tick_params(axis='both', which='major', labelsize=20, length=10, width=2, colors='black', direction='out')
    ax.tick_params(axis='both', which='minor', labelsize=1, length=0.5, width=0.5, colors='black', direction='out')
    
# Add labels (a), (b), (c), ... to each subplot
labels = ['(a)', '(b)', '(c)', '(d)', '(e)', '(f)']
for i, ax in enumerate(axs.flat):
    ax.text(0.02, 0.91, labels[i], transform=ax.transAxes,
            fontsize=25, va='top',ha="left")


for ax in axs.flat:
    ax.label_outer() 

fig.text(-0.03, 0.5, 'Fidelity', va='center', rotation='vertical', fontsize=25)
fig.text(0.44, -0.01, r"Time in unit of $\hbar$", va='center', rotation='horizontal', fontsize=25)

handles, labels = axs[0, 0].get_legend_handles_labels()
legend = fig.legend(handles, labels, loc='upper center', fontsize=18, ncol=3, bbox_to_anchor=(0.52, 1.05), handleheight=1.6, labelspacing=0.1, frameon=True)

legend.get_frame().set_edgecolor('black')
legend.get_frame().set_linewidth(2)

plt.tight_layout(rect=[0, 0, 1, 0.96])

fig.savefig('noise_heisen.png', dpi=500, bbox_inches='tight', pad_inches=0.3)
plt.show()
