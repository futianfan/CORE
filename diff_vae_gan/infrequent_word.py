import torch
import torch.nn as nn
import torch.optim as optim
import torch.optim.lr_scheduler as lr_scheduler
from torch.utils.data import DataLoader
from torch.autograd import Variable

import math, random, sys
import numpy as np
import argparse
from collections import deque
import cPickle as pickle

from fast_jtnn import *
import rdkit


parser = argparse.ArgumentParser()
parser.add_argument('--test', required=True)
parser.add_argument('--vocab', required=True)
parser.add_argument('--model', required=True)



