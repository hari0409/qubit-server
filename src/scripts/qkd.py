from qiskit import QuantumCircuit, Aer, transpile, assemble
from numpy.random import randint
import numpy as np

def gen_bases(n):
    bases = randint(2, size=n)
    return bases

def encode_message(bits, bases, rows, cols):
    message = []
    for i in range(cols):
        submessage=[]
        qc = QuantumCircuit(1,1)
        if bases[i] == 0: # Prepare qubit in Z-basis
            if bits[0][i] == 0:
                pass 
            else:
                qc.x(0)
        else: # Prepare qubit in X-basis
            if bits[0][i] == 0:
                qc.h(0)
            else:
                qc.x(0)
                qc.h(0)
        qc.barrier()
        message.append(qc)
    for i in range(1,rows):
      message.append(bits[i])
    return message