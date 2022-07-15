from setuptools import find_packages, setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension


setup(
    name='lltm',
    version='0.1.0',
    packages=find_packages(),
    ext_modules=[
        CUDAExtension('lltm._ext', [
            './lltm/lltm_cuda.cpp',
            './lltm/lltm_cuda_kernel.cu',
        ]),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })
