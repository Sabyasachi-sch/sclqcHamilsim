import numpy as np

from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

from scipy.sparse import csc_array as spcsc
from scipy.sparse import kron as spkrn
from scipy.sparse.linalg import expm

import CNOT_connection as CNOT_conc


def qubit_cktx(theta, qno):
    qc = QuantumCircuit(qno)
    qc.rx(-theta, 0)
    return qc


X=np.array([[0, 1],[1, 0]]);
Y=np.array([[0, -1j],[1j, 0]]);
Z=np.array([[1, 0],[0, -1]]);
I=np.array([[1, 0],[0, 1]]);

had_mat = 1/(2**0.5)*np.array([[1,1],[1,-1]])

X_sp = spcsc(X)
Y_sp = spcsc(Y)
Z_sp = spcsc(Z)
I_sp = spcsc(I)

had_mat_sp = spcsc(had_mat)

def XX_Block_diag(input_str, q_no):
    if input_str[:-1] == 'I' * (len(input_str) - 1) and input_str[-1] == 'X':
        return np.eye(2**q_no)
    
    b_val = CNOT_conc.op_cnot(input_str, q_no)[0]
    cnot_arr = CNOT_conc.output_cnot(input_str, q_no)
    
    qc = QuantumCircuit(q_no)
    
    if b_val % 2 == 0:  # Even
        qc.cnot(max(cnot_arr), 0)
        
        for posn in cnot_arr:
            qc.cnot(0, posn)
        
        qc.cnot(max(cnot_arr), 0)
        
    else:
        for posn in cnot_arr:
            qc.cnot(0, posn)
    
    U = Operator(qc)
    
    return U.data

def generate_kron(input_str):
    matrix_map = {
        'I': I,
        'X': X_sp,  # Use Pauli X for 'X'
        }

    result = matrix_map[input_str[0]]

    for char in input_str[1:]:
        result = spkrn(result, matrix_map[char])
    return spcsc(result)

def cktXX2(input_str, q_no, argm, time_step):

    Hamil = generate_kron(input_str)
    
    def M2_XX(q_no):
        M2_mat = expm((-1j)*argm*time_step*Hamil);
        return M2_mat
    
    qcx = qubit_cktx(-2*argm*time_step, q_no)
    CNOT_gates_on_sides = spcsc(XX_Block_diag(input_str, q_no))
    Ux = Operator(qcx)
    resultant_mat_ph = spcsc(Ux.data)
    
    
    
    resultant_mat0 = spcsc( CNOT_gates_on_sides.dot(resultant_mat_ph.dot(CNOT_gates_on_sides))) 
    
    final_result_mat = spcsc(resultant_mat0)
    
    def frb_norm(res_mat,ip_mat):
        
        Msub = ((res_mat)-(ip_mat));
        Msub_H = (spcsc.conjugate(Msub)).T

        N2_res = (10**7)*(spcsc.trace(Msub.dot(Msub_H)))**0.5
        
        return N2_res

    return spcsc(final_result_mat), frb_norm(resultant_mat0,M2_XX(q_no))/10**7

##### Example: To determine the matrix corresponding to the Scalable Circuit model for a Pauli-X String

##### ckt_mat returns the circuit matrix in sparse format and error returns the Frobenius norm.

ckt_mat, error = cktXX2("XXIXIX", 6, 0.08, 0.001)

print("Frobenius norm:", error)

