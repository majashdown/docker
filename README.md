# Docker

Dockerfiles for creating images:

* shifter-intelpython: image containing MPI and the Intel distribution
  for Python, suitable for use with Shifter at NERSC.  This is
  intended as a basis for other images, so only a minimal set of
  Python packages is installed.

* shifter-intelpython-hello: example of using the shifter-intelpython
  image.  A simple 'Hello world' Python script installed on top of it.

* shifter-intelpython-healpy: image with the numpy, scipy and healpy
  packages, and their dependencies, installed on top of the
  shifter-intelpython image.
