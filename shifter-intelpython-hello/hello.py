from mpi4py import MPI

comm = MPI.COMM_WORLD

fmt = 'Hello, parallel world! I am process {} of {}.'
print(fmt.format(comm.rank, comm.size))
