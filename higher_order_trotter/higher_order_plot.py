import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
import labellines

import os

os.chdir('C:/Users/User/Work_space/python_rohit/hamil_sim/All_plot_code_APL/higher_order_trotter')

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.linewidth'] = 1
plt.rcParams["axes.edgecolor"] = "black"


del_t= 0.001
time_val=del_t

time_array = del_t*(np.array([1,2,3,4,6,8,10,13,18,24,32,42,56,75,100,133,178,237,316,422,562,750,1000]))


Qubit_no = [2,3,4,5,6,7,8,9,10,12,14]

Frb_norm4_1 = sparse.load_npz("1st_order/4qubit_frb_norm.npz").toarray()[0]
Frb_norm6_1 = sparse.load_npz("1st_order/6qubit_frb_norm.npz").toarray()[0]
Frb_norm8_1 = sparse.load_npz("1st_order/8qubit_frb_norm.npz").toarray()[0]


Frb_norm4_2 = sparse.load_npz("2nd_order/4qubit_frb_norm.npz").toarray()[0]
Frb_norm6_2 = sparse.load_npz("2nd_order/6qubit_frb_norm.npz").toarray()[0]
Frb_norm8_2 = sparse.load_npz("2nd_order/8qubit_frb_norm.npz").toarray()[0]

Frb_norm4_4 = sparse.load_npz("4th_order/4qubit_frb_norm.npz").toarray()[0]
Frb_norm6_4 = sparse.load_npz("4th_order/6qubit_frb_norm.npz").toarray()[0]
Frb_norm8_4 = sparse.load_npz("4th_order/8qubit_frb_norm.npz").toarray()[0]

################## ckt ############################
Frb_norm4_1_ckt = sparse.load_npz("1st_order/4qubit_frb_norm_ckt.npz").toarray()[0]
Frb_norm6_1_ckt = sparse.load_npz("1st_order/6qubit_frb_norm_ckt.npz").toarray()[0]
Frb_norm8_1_ckt = sparse.load_npz("1st_order/8qubit_frb_norm_ckt.npz").toarray()[0]


Frb_norm4_2_ckt = sparse.load_npz("2nd_order/4qubit_frb_norm_ckt.npz").toarray()[0]
Frb_norm6_2_ckt = sparse.load_npz("2nd_order/6qubit_frb_norm_ckt.npz").toarray()[0]
Frb_norm8_2_ckt = sparse.load_npz("2nd_order/8qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm4_4_ckt = sparse.load_npz("4th_order/4qubit_frb_norm_ckt.npz").toarray()[0]
Frb_norm6_4_ckt = sparse.load_npz("4th_order/6qubit_frb_norm_ckt.npz").toarray()[0]
Frb_norm8_4_ckt = sparse.load_npz("4th_order/8qubit_frb_norm_ckt.npz").toarray()[0]

#######################################################################

Frb_norm_array_1 = np.array([Frb_norm4_1, Frb_norm6_1, Frb_norm8_1])
Frb_norm_array_2 = np.array([Frb_norm4_2, Frb_norm6_2, Frb_norm8_2])
Frb_norm_array_4 = np.array([Frb_norm4_4, Frb_norm6_4, Frb_norm8_4])

Frb_norm_array_1_ckt = np.array([Frb_norm4_1_ckt, Frb_norm6_1_ckt, Frb_norm8_1_ckt])
Frb_norm_array_2_ckt = np.array([Frb_norm4_2_ckt, Frb_norm6_2_ckt, Frb_norm8_2_ckt])
Frb_norm_array_4_ckt = np.array([Frb_norm4_4_ckt, Frb_norm6_4_ckt, Frb_norm8_4_ckt])

fig = plt.figure(figsize=(10,8))

label_arr = ['n=4','n=6','n=8']
marker_arr = ['o','^','<']

color_arr = ["#8b02b5", "#fc0313","#11c208"]

alpha_arr = [0.48, 0.56, 0.82]

alpha_arr1 = [0.38, 0.42, 0.46]


for i in range(len(Frb_norm_array_1)):
    plt.plot(time_array,Frb_norm_array_1[i],color=color_arr[0],lw="2", marker=marker_arr[i],markersize=6, label=label_arr[i], alpha=alpha_arr[i])
    plt.plot(time_array,Frb_norm_array_1_ckt[i],color="black",ls="--",lw="3", alpha=alpha_arr1[i])
    
for i in range(len(Frb_norm_array_2)):
    plt.plot(time_array,Frb_norm_array_2[i],color=color_arr[1],lw="2", marker=marker_arr[i],markersize=6, label=label_arr[i], alpha=alpha_arr[i])
    plt.plot(time_array,Frb_norm_array_2_ckt[i],color="black",ls="--",lw="3", alpha=alpha_arr1[i])
    
for i in range(len(Frb_norm_array_4)):
    plt.plot(time_array,Frb_norm_array_4[i],color=color_arr[2],lw="2", marker=marker_arr[i],markersize=6, label=label_arr[i], alpha=alpha_arr[i])
    plt.plot(time_array,Frb_norm_array_4_ckt[i],color="black",ls="--",lw="3", alpha=alpha_arr1[i])
    
    
plt.xscale("log")
plt.yscale("log")

plt.xlabel(r"Time in unit of $\hbar$",fontsize=25)
plt.ylabel("Error",fontsize=25)

plt.legend(loc="lower right",fontsize=17, ncol=3,handleheight=1.6, labelspacing=0.005)

plt.ylim(1.e-16,1.e-1)
plt.xlim(9.5*10**(-4),1.2)

# plt.tick_params(axis='both',which='major', width=2)
plt.tick_params(axis='both', which='major', labelsize=20, length=10, width=2, colors='black', direction='out')
plt.tick_params(axis='both', which='minor', labelsize=1, length=0.5, width=0.5, colors='black', direction='out')

plt.gca().spines['right'].set_linewidth(2.5)  
plt.gca().spines['top'].set_linewidth(2.5)   
plt.gca().spines['bottom'].set_linewidth(2.5)
plt.gca().spines['left'].set_linewidth(2.5)  

fig.savefig('Higher_order_trotter.png', bbox_inches='tight', dpi=300)


