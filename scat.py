# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 17:00:06 2018

@author: Rabbit
"""


# mpiexec -n 18 python mpiscatter.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    shared = [1,23,5,6,7,8,9,9,666,8,97,5,7,88,97,8,9,0]
else:
    shared =None

recvbuf = comm.scatter(shared, root=0)
print("rank = ", rank,"  data= ", recvbuf )