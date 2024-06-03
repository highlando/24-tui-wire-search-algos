import numpy as np
import time

from all_sortingsv import get_array_sort

Ntimes = 10
Nsize = 1000
nameidx = ['ps', 'ea', 'cv', 'eo', 'tbd']

for nameid in nameidx:
    testvec = np.linspace(0, 1, 101)
    testres = np.copy(testvec[::-1])
    sortv = get_array_sort(nameid=nameid)
    if np.linalg.norm(sortv(testvec)-testres) < 1e-12:
        print(f'{nameid}: test passed')
    else:
        print(f'{nameid}: test not passed')
        # testvec = np.linspace(0, 1, 101)
        # print(sortv(testvec))
        pass
        # raise RuntimeWarning('please double check')

    timings = []
    for ntim in range(Ntimes):
        testvec = np.random.randn(Nsize)
        strtt = time.time()
        resv = sortv(testvec)
        endtt = time.time()
        timings.append(endtt-strtt)
    timearray = np.array(timings)
    print(f'{nameid}: best time {np.min(timearray)}')
    print(f'{nameid}: wrst time {np.max(timearray)}')
