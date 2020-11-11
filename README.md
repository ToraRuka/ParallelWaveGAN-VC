# Parallel WaveGAN VC implementation with Pytorch

This repository provides **UNOFFICIAL** [Unsupervised Cross-Domain Singing Voice Conversion](https://arxiv.org/abs/2008.02830) implementations with Pytorch.  
Base code for this repository is forked from [kan-bayashi/ParallelWaveGAN](https://github.com/kan-bayashi/ParallelWaveGAN)

The goal of this repository is to provide vocoder-free voice conversion.


## What's new

- 2020/11/11 :birthday: Birth-day of this project 

## Requirements

This repository is tested on Ubuntu 16.04 with a GPU Titan V.

- Python 3.6+
- Cuda 10.0+
- CuDNN 7+
- NCCL 2+ (for distributed multi-gpu training)
- libsndfile (you can install via `sudo apt install libsndfile-dev` in ubuntu)
- jq (you can install via `sudo apt install jq` in ubuntu)
- sox (you can install via `sudo apt install sox` in ubuntu)

Different cuda version should be working but not explicitly tested.  
All of the codes are tested on Pytorch 1.0.1, 1.1, 1.2, 1.3.1, 1.4, 1.5.1, and 1.7.

Pytorch 1.6 works but there are some issues in cpu mode (See #198).

## Setup

You can select the installation method from two alternatives.

### A. Use pip

```bash
$ git clone https://github.com/ToraRuka/ParallelWaveGAN-VC.git
$ cd ParallelWaveGAN-VC
$ pip install -e .
# If you want to use distributed training, please install
# apex manually by following https://github.com/NVIDIA/apex
$ ...
```
Note that your cuda version must be exactly matched with the version used for the pytorch binary to install apex.  
To install pytorch compiled with different cuda version, see `tools/Makefile`.

### B. Make virtualenv

```bash
$ git clone https://github.com/kan-bayashi/ParallelWaveGAN.git
$ cd ParallelWaveGAN/tools
$ make
# If you want to use distributed training, please run following
# command to install apex.
$ make apex
```

Note that we specify cuda version used to compile pytorch wheel.  
If you want to use different cuda version, please check `tools/Makefile` to change the pytorch wheel to be installed.

## Recipe

This repository provides [Kaldi](https://github.com/kaldi-asr/kaldi)-style recipes, as the same as [ESPnet](https://github.com/espnet/espnet).  
Currently, the following recipes are supported.

- [LJSpeech](https://keithito.com/LJ-Speech-Dataset/): English female speaker


To run the recipe, please follow the below instruction.

```bash
# Let us move on the recipe directory
$ cd egs/ljspeech/vc1

# Run the recipe from scratch
$ ./run.sh

# You can change config via command line
$ ./run.sh --conf <your_customized_yaml_config>

# You can select the stage to start and stop
$ ./run.sh --stage 2 --stop_stage 2

# If you want to specify the gpu
$ CUDA_VISIBLE_DEVICES=1 ./run.sh --stage 2

# If you want to resume training from 10000 steps checkpoint
$ ./run.sh --stage 2 --resume <path>/<to>/checkpoint-10000steps.pkl
```

See more info about the recipes in [this README](./egs/README.md).

## Speed
TBA

## Results
TBA

## How-to-use pretrained models
TBA

## References

- [Unsupervised Cross-Domain Singing Voice Conversion](https://arxiv.org/abs/2008.02830)
- [Parallel WaveGAN](https://arxiv.org/abs/1910.11480)
- [r9y9/wavenet_vocoder](https://github.com/r9y9/wavenet_vocoder)
- [LiyuanLucasLiu/RAdam](https://github.com/LiyuanLucasLiu/RAdam)
- [MelGAN](https://arxiv.org/abs/1910.06711)
- [descriptinc/melgan-neurips](https://github.com/descriptinc/melgan-neurips)
- [Multi-band MelGAN](https://arxiv.org/abs/2005.05106)


## Acknowledgement

The author would like to thank Ryuichi Yamamoto ([@r9y9](https://github.com/r9y9)) for his great repository, paper, and valuable discussions.
also autor would like to thank Tomoki Hayashi ([@kan-bayashi](https://github.com/kan-bayashi)) for his greeeeat repository.

## Author

Jaegeon Jo ([@ToraRuka](https://github.com/ToraRuka))  
E-mail: `toraruka623<at>gmail.com`
