# shifter-intelpython-hello

This Dockerfile is an example of how to use the shifter-intelpython
image as a basis to create an image containing a Python script to run
with Shifter at NERSC.  In this case, we add a simple 'Hello world'
script.

To run the image, for example, on Cori....

Pull the image from Docker:
```
shifterimg pull docker:majashdown/shifter-intelpython-hello:latest
```
Launch an interactive job:
```
salloc -N 1 -C haswell -p debug -t 00:30:00 --image docker:majashdown/shifter-intelpython-hello:latest
```
Run the script in serial like this:
```
shifter python /home/hello/hello.py
```
or in parallel like this:
```
srun -n 32 -c 2 shifter python /home/hello/hello.py
```
