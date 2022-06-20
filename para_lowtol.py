import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import os
import time
from concurrent.futures import ProcessPoolExecutor
from Minimization_lowtol import minimization
np.set_printoptions(suppress = True)

with open('re_starts.pkl','rb') as f:
    start = pickle.load(f)

start_time = time.time()
if __name__ == '__main__':
    with ProcessPoolExecutor() as pool:
        results = pool.map(minimization, start)
    results = [r for r in results]
run_time = time.time() - start_time
print(run_time)
with open('output_re_starts.pkl', 'wb') as f:
       pickle.dump(results, f)