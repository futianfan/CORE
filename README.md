# CORE: Automatic Molecule Optimization using Copy and Refine Strategy (AAAI 2020)



## Requirements (Following Graph2Graph)
* Python == 2.7
* RDKit >= 2017.09
* PyTorch >= 0.4.0
* Numpy
* scikit-learn

The code has been tested under python 2.7 with pytorch 0.4.1. 

## Quick Start (Following Graph2Graph)
The tutorial of training and testing our variational junction tree encoder-decoder is in [diff_vae/README.md](./diff_vae).

A quick summary of different folders:
* `data/` contains the training, validation and test set of logP, QED and DRD2 tasks described in the paper.
* `fast_jtnn/` contains the implementation of junction tree encoder-decoder.
* `diff_vae/` includes the training and decoding script of variational junction tree encoder-decoder ([README](./diff_vae)).
* `diff_vae_gan/` includes the training and decoding script of adversarial training module ([README](./diff_vae_gan)).
* `props/` is the property evaluation module, including penalized logP, QED and DRD2 property calculation.
* `scripts/` provides evaluation and data preprocessing scripts.


## Implementation of CORE

* `fast_jtnn/xxx.py` 

This repo is adapted from [Graph2Graph](https://github.com/wengong-jin/iclr19-graph2graph). 


## Contact
Tianfan Fu (futianfan@gmail.com)

