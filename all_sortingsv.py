import numpy as np


def get_array_sort(nameid=None):

    if nameid == 'ps':
        def array_sort(v):
            srtd_v=[]
            #ma=0
            j=None
            L=len(v)
            #print(L)
            for h in range (L):
                ma=-np.inf
                for i in range(L-1):
                    if v[i]>v[i+1]:
                        if ma<v[i]:
                            ma=v[i]
                            # print(ma)
                            j=i
                    if v[i]<v[i+1]:
                        if ma<v[i+1]:
                            ma=v[i+1]
                            #J print(ma)
                            j=i+1
                v[j]=-np.inf
                # print(v)
                srtd_v.append(ma)
            
            return srtd_v

    if nameid == 'ea':
        def array_sort(v):
            for i in range(len(v)):
                for j in range(i, len(v)):
                    if v[i] > v[j]:
                        a = v[i]
                        v[i] = v[j]
                        v[j] = a
            return v

    if nameid == 'cv':
        def array_sort(v):
            n=len(v)
            for b in range(1,n):
               for k in range(0,n-b):
                 if v[k] >  v[k+1]:
                   c = v[k]
                   v[k] = v[k+1]
                   v[k+1] = c
            return v[::-1]

    if nameid == 'eo':
        def array_sort(Array):
            length = len(Array)
            sortedArray = [None]*length
            for i in range(length):
                m = max(Array)
                sortedArray[i] = m
                del Array[Array.index(m)]
            return sortedArray

    return array_sort
