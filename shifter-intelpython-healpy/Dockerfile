# This Dockerfile uses the shifter-intelpython image as a basis to
# create an image containing the numpy, scipy and healpy packages, and
# their dependencies.  Healpy is installed using pip, because it is
# not available from the standard channels.

FROM majashdown/shifter-intelpython:latest

RUN conda install -y -q numpy scipy matplotlib astropy

RUN pip install healpy
