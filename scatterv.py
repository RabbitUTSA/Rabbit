# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 11:30:37 2018

@author: Rabbit
"""

# for correct performance, run unbuffered with 3 processes:
	# mpiexec -n 3 python26 scratch.py -u
	import numpy 
	from mpi4py import MPI 
	comm = MPI.COMM_WORLD 
	rank = comm.Get_rank() 
	
	if rank == 0: 
		x = numpy.linspace(0,100,11) 
	else: 
		x = None 
	
	if rank == 2: 
		xlocal = numpy.zeros(9) 
	else: 
		xlocal = numpy.zeros(1) 
	
	if rank ==0:
		print "Scatter"
	comm.Scatterv([x,(1,1,9),(0,1,2),MPI.DOUBLE],xlocal) 
	print ("process " + str(rank) + " has " +str(xlocal))
	
	comm.Barrier()
	if rank == 0:
		print "Gather"
		xGathered = numpy.zeros(11)
	else:
		xGathered = None
	comm.Gatherv(xlocal,[xGathered,(1,1,9),(0,1,2),MPI.DOUBLE])
	print ("process " + str(rank) + " has " +str(xGathered))