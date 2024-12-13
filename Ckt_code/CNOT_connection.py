#### Defining CNOT Gate Connections Using the Permutation Matrix Theorem as Described in the Paper


def assign_x_i(s):
    result = ""
    for char in s:
        if char == 'Z' or char == 'X' or char == 'Y':
            result += '1'
        elif char == 'I':
            result += '0'
    return result


def op_cnot(input_str, q_no):
    binary_int = assign_x_i(input_str)
    b = int(str(binary_int), 2)


    if b % 2 == 0:  # Even
        new_string = b // 2
    else:  # Odd
        new_string = (b - 1) // 2

    binary_new_string = bin(new_string)[2:] 

    position_array = []


    for i, bit in enumerate(reversed(binary_new_string)):
        if bit == '1':
            position_array.append(i)  
    new_array1 = [q_no - j - 1 for j in position_array]
    m1 = [min(new_array1)]
    return b, new_array1, m1


def output_cnot(input_str, q_no):
    b_val, new_array, m = op_cnot(input_str, q_no)
  
    if b_val % 2 == 0:  # Even
        qiskit_cnot1 = [q_no-i for i in new_array]
        return qiskit_cnot1
        
    else:  # Odd
        qiskit_cnot = [q_no-i for i in new_array]
        return qiskit_cnot



