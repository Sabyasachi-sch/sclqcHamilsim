import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
import labellines

plt.rcParams['font.family'] = 'serif'
plt.rcParams['axes.linewidth'] = 1
plt.rcParams["axes.edgecolor"] = "black"

del_t= 0.001
time_val=del_t

time_array = del_t*(np.array([1,2,3,4,6,8,10,13,18,24,32,42,56,75,100,133,178,237,316,422,562,750,1000]))


Qubit_no = [2,3,4,5,6,7,8,9,10,12,14]


Frb_norm4 = sparse.load_npz("4qubit_frb_norm.npz").toarray()[0]

Frb_norm5 = sparse.load_npz("5qubit_frb_norm.npz").toarray()[0]

Frb_norm6 = sparse.load_npz("6qubit_frb_norm.npz").toarray()[0]

Frb_norm7 = sparse.load_npz("7qubit_frb_norm.npz").toarray()[0]

Frb_norm8 = sparse.load_npz("8qubit_frb_norm.npz").toarray()[0]

Frb_norm9 = sparse.load_npz("9qubit_frb_norm.npz").toarray()[0]

Frb_norm10 = sparse.load_npz("10qubit_frb_norm.npz").toarray()[0]

################################# ckt  ###########################################

Frb_norm4_ckt =  sparse.load_npz("4qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm5_ckt = sparse.load_npz("5qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm6_ckt = sparse.load_npz("6qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm7_ckt = sparse.load_npz("7qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm8_ckt = sparse.load_npz("8qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm9_ckt = sparse.load_npz("9qubit_frb_norm_ckt.npz").toarray()[0]

Frb_norm10_ckt = sparse.load_npz("10qubit_frb_norm_ckt.npz").toarray()[0]


Frb_norm_array = np.array([Frb_norm4, Frb_norm5, Frb_norm6, Frb_norm7, Frb_norm8, Frb_norm9, Frb_norm10])

Frb_norm_array_ckt = np.array([Frb_norm4_ckt, Frb_norm5_ckt, Frb_norm6_ckt, Frb_norm7_ckt, Frb_norm8_ckt, Frb_norm9_ckt, Frb_norm10_ckt])

fig = plt.figure(figsize=(10,8))

label_arr = ['n=4','n=5','n=6','n=7','n=8','n=9','n=10']
marker_arr = ['o','P','<','D','x','^','>']

color_arr = ["#8b02b5", "#443bff","#11c208", "#a30232", "#fc0313" , "#0b9c62","#ed800c"]

alpha_arr = [0.48, 0.56, 0.82, 0.70, 0.78, 0.86, 0.93, 1.0]

alpha_arr1 = [0.38, 0.42, 0.46, 0.50, 0.54, 0.58, 0.62, 0.66]


for i in range(0,7):
    plt.loglog(time_array,Frb_norm_array[i],color=color_arr[i],lw="2", marker=marker_arr[i],markersize=6, label=label_arr[i], alpha=alpha_arr[i])
    plt.loglog(time_array,Frb_norm_array_ckt[i],color="black",ls="--",lw="3", alpha=alpha_arr1[i])


plt.text(.03, .97, '(b)', fontsize=20, ha='left', va='top', transform=plt.gca().transAxes)

plt.xlabel(r"Time in unit of $\hbar$",fontsize=25)
plt.ylabel("Error",fontsize=25)


plt.legend(loc="lower right",fontsize=20, ncol=2,handleheight=1.6, labelspacing=0.005)

# plt.ylim(4.e-15,1.e-12)
# plt.xlim(7*10**(-4),1.2)


plt.tick_params(axis='both', which='major', labelsize=20, length=10, width=2, colors='black', direction='out')
plt.tick_params(axis='both', which='minor', labelsize=1, length=0.5, width=0.5, colors='black', direction='out')

plt.gca().spines['right'].set_linewidth(2.5)  
plt.gca().spines['top'].set_linewidth(2.5)   
plt.gca().spines['bottom'].set_linewidth(2.5) 
plt.gca().spines['left'].set_linewidth(2.5) 

fig.savefig('Heisen_ising_long.png', dpi=300)