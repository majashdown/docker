FROM majashdown/shifter-intelpython:latest

# Use conda to install numpy, scipy, matplotlib and astropy, with
# their dependencies.

RUN conda install -y -q numpy scipy matplotlib astropy

# Use pip to install healpy, because it is not available from the
# regular channels.

RUN pip install healpy
