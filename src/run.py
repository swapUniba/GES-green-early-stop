import os
import time

# define models and datasets
models = ['BPR', 'CFKG', 'CKE', 'DMF', 'KGCN', 'KGNNLS', 'LINE', 'MultiDAE', 'LightGCN', 'NGCF', 'DGCF']
datasets = ['movielens_1m']

# define GES parameters
max_emission_step = 7       # treshold
ratio_tolerance = 40        # tolerance

# run models on datasets with GES
for dataset in datasets:
    for model in models:
        os.system(f"python train_ges.py --dataset={dataset} --model={model} --max_emission_step={max_emission_step} --ratio_tolerance={ratio_tolerance}")