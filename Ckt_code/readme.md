# Research Supplementary Materials

This repository contains supplementary materials and code relevant to the research study. The datasets and detailed information for a complete understanding of the research can be obtained from the corresponding author upon reasonable request.

## Included Resources

1. **Example Code for Circuit Construction**  
   An example code for constructing a circuit with a Pauli string is provided. This enables users to generate scalable circuit frameworks for any desired unitary operation.

2. **Folder Contents**  
   - **`CNOT_connection`**  
     Defines the CNOT gate connections using the Permutation Matrix Theorem as described in the paper.

   - **`ckt_diag_sp`**  
     Contains the matrix corresponding to the scalable circuit model for a Pauli-Z string.  
     - **Output:** Circuit matrix in sparse format.  
     - **Error:** Frobenius norm of the Pauli-Z string.

   - **`ckt_with_X_sp`**  
     Contains the matrix corresponding to the scalable circuit model for a Pauli-X string.  
     - **Output:** Circuit matrix in sparse format.  
     - **Error:** Frobenius norm of the Pauli-X string.

   - **`ckt_with_Y_sp`**  
     Contains the matrix corresponding to the scalable circuit model for a Pauli-Y string.  
     - **Output:** Circuit matrix in sparse format.  
     - **Error:** Frobenius norm of the Pauli-Y string.  

This code is used to generate the figures outlined in the research.
