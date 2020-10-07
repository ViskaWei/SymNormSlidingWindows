from util import *
from dataset import *
import numpy as np
import logging

n, m, w =2, 1000, 200
assert m > w
wId = m-w
c=int(np.log10(m))
# c = 2
r=1000
device='cuda'

stream, exactL2, exactL2w = create_stream(n,m,w)
uniformL2w =uniform_sampling(stream, w, sRate=0.1)

streamTr=torch.tensor(stream, dtype=torch.int64)
streamTr0=streamTr[:10]

def main():
    print('exact vs uniform L2w', exactL2w, uniformL2w)
    sketchNorm = run(streamTr,c,r,device, wId)
    print('sketch L2w', sketchNorm)
    print('exact L2', exactL2)


main()