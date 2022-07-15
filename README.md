# Conda build examples

Conda-build contains commands and tools to use conda to build your own packages. It also provides helpful tools to constrain or pin versions in recipes. Building a conda package requires installing conda-build and creating a conda recipe. You then use the conda build command to build the conda package from the conda recipe.

## Installation

Step1: Create a conda environment

```bash
conda create -n conda-build-examples python=3.7
```

Step2: Install conda-build

```bash
conda install conda-build
```

## Build packages

### example1

This is a simple example of how to build a conda package.

```bash
git clone https://github.com/zhouzaida/conda-build-examples
cd conda-build-examples/example1
conda build ./recipe
```

### example2

This example is used to demonstrate how to infer the corresponding cudatoolkit version when installing PyTorch with conda.

```bash
git clone https://github.com/zhouzaida/conda-build-examples
cd conda-build-examples/example2
conda build ./recipe -c pytorch
```

## Upload packages

Step1: Register an acount at https://anaconda.org/account/login

Step2: Install anaconda-client

```bash
conda install anaconda-client
```

Step3: Logging anaconda in terminal

```bash
ananconda login
```

Step4: Upload the package

```bash
anaconda upload anaconda upload /path/to/lltm-0.1.0-py3.7_torch1.10_cuda11.3_cudnn8.2.0_0.tar.bz2
```

**Note**: Replace /path/to/ with the actual path where you stored the package.

Step5: See packages at https://anaconda.org/zhouzaida/repo

## Test packages

### Test example1

```bash
conda install npop -c zhouzaida
```

### Test example2

I uploaded two versions of lltm build with different PyTorch and CUDA versions.

The following commands will install lltm from lltm-0.1.0-py3.7_torch1.10_cuda11.3_cudnn8.2.0_0.tar.bz2.

```bash
conda install pytorch==1.10.0 cudatoolkit=11.3 -c pytorch
conda install lltm -c zhouzaida
```

The following commands will install lltm from lltm-0.1.0-py3.7_torch1.12_cuda11.3_cudnn8.3.2_0.tar.bz2.

```bash
conda install pytorch==1.12.0 cudatoolkit=11.3 -c pytorch
conda install lltm -c zhouzaida
```

## References

- [Conda-build recipes](https://docs.conda.io/projects/conda-build/en/latest/concepts/recipe.html)

- [uploading-conda-packages](https://docs.anaconda.com/anacondaorg/user-guide/tasks/work-with-packages/#uploading-conda-packages)
