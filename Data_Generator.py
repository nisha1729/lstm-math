from itertools import product
from random import sample
import argparse
import math
import operator

parser = argparse.ArgumentParser(description='Data Generator.')
parser.add_argument('-max', '--maximum_integer', type=int, default=1000)
parser.add_argument('-N', '--number_of_instances', type=int, default=1000000)
parser.add_argument('--train_fraction', type=float, default=0.8)
parser.add_argument('--val_fraction', type=float, default=0.1)
args = parser.parse_args()

ops = {"+": operator.add, "-": operator.sub}
max = args.maximum_integer          #1000
N = args.number_of_instances        #100K
train_frac = args.train_fraction    #80K
val_frac = args.val_fraction        # 10K
ds = sample(list(product(range(0, max), ["+", "-"], range(0, max))), N)
# print(ds[0:5])
train_data = ds[: math.floor(train_frac * N)]
# print(train_data[0:5])

val_data = ds[math.floor(train_frac * N): math.floor((train_frac + val_frac) * N)]
test_data = ds[math.floor((train_frac + val_frac) * N):]
# print(val_data)
# print(test_data)
for data in [train_data[0:5]]:
    if data != []:
        for instance in data:
            i1, op, i2 = instance
            eqn = str(i1) + " " + op + " " + str(i2)
            print(eqn)
