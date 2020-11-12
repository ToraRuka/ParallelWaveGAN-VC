#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Setup Parallel WaveGAN libarary."""

import os
import pip
import sys

from distutils.version import LooseVersion
from setuptools import find_packages
from setuptools import setup

if LooseVersion(sys.version) < LooseVersion("3.6"):
    raise RuntimeError(
        "parallel-wavegan-vc requires Python>=3.6, "
        "but your Python is {}".format(sys.version))
if LooseVersion(pip.__version__) < LooseVersion("19"):
    raise RuntimeError(
        "pip>=19.0.0 is required, but your pip is {}. "
        "Try again after \"pip install -U pip\"".format(pip.__version__))

requirements = {
    "install": [
        "torch>=1.0.1",
        "setuptools>=38.5.1",
        "librosa>=0.8.0",
        "soundfile>=0.10.2",
        "tensorboardX>=1.8",
        "matplotlib>=3.1.0",
        "PyYAML>=3.12",
        "tqdm>=4.26.1",
        "kaldiio>=2.14.1",
        "h5py>=2.9.0",
        "yq>=2.10.0",
        "gdown",
        "torchaudio",
        "torchcrepe",
        "toml",
    ],
    "setup": [
        "numpy",
        "pytest-runner",
    ],
    "test": [
        "pytest>=3.3.0",
        "hacking>=1.1.0",
        "flake8>=3.7.8",
        "flake8-docstrings>=1.3.1",
    ]
}
entry_points = {
    "console_scripts": [
        "parallel-wavegan-vc-preprocess=parallel_wavegan_vc.bin.preprocess:main",
        "parallel-wavegan-vc-compute-statistics=parallel_wavegan_vc.bin.compute_statistics:main",
        "parallel-wavegan-vc-normalize=parallel_wavegan_vc.bin.normalize:main",
        "parallel-wavegan-vc-train=parallel_wavegan_vc.bin.train:main",
        "parallel-wavegan-vc-decode=parallel_wavegan_vc.bin.decode:main",
    ]
}

install_requires = requirements["install"]
setup_requires = requirements["setup"]
tests_require = requirements["test"]
extras_require = {k: v for k, v in requirements.items()
                  if k not in ["install", "setup"]}

dirname = os.path.dirname(__file__)
setup(name="parallel_wavegan_vc",
      version="0.4.8",
      url="https://github.com/ToraRuka/ParallelWaveGAN-VC",
      author="Jaegeon Jo",
      author_email="toraruka623@gmail.com",
      description="Parallel WaveGAN VC implementation",
      long_description=open(os.path.join(dirname, "README.md"),
                            encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      license="MIT License",
      packages=find_packages(include=["parallel_wavegan_vc*"]),
      install_requires=install_requires,
      setup_requires=setup_requires,
      tests_require=tests_require,
      extras_require=extras_require,
      entry_points=entry_points,
      classifiers=[
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Intended Audience :: Science/Research",
          "Operating System :: POSIX :: Linux",
          "License :: OSI Approved :: MIT License",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      )
