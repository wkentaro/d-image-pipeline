================
D Image Pipeline
================

* PC environment
::

  % lsb_release -a
  No LSB modules are available.
  Distributor ID:	Ubuntu
  Description:	Ubuntu 14.04.3 LTS
  Release:	14.04
  Codename:	trusty
  % lspci | grep VGA
  01:00.0 VGA compatible controller: NVIDIA Corporation Device 13c0 (rev a1)

* Install cuda 7.5 from `here <https://developer.nvidia.com/cuda-downloads>`_ .
* Add below environment variables
::

  export CUDA_ROOT=/usr/local/cuda
  export PATH=/usr/local/cuda/bin:$PATH
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64
