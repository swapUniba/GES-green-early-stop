"""
A collection of utility functions
"""
import os
from pathlib import Path
import torch
import csv
from datetime import datetime
from functools import reduce
from sys import platform
import pandas as pd


def create_folders(datasets, models, first_level_folders):
	"""Create folder structure in this order:
		│
		├── first_level_folders
		│   │
		│   └── datasets
		│   	│
		│   	└── models
	Args:
		first_level_folders (list): Folders root in which create structure.
		datasets (list): First level subfolders.
		models (list): Second level subfolders.
	Returns:
		None.
	"""
	for f in first_level_folders:
		for d in datasets:
			path_base = os.path.join(f, d)
			if not os.path.isdir(path_base):
				Path(path_base).mkdir(parents=True, exist_ok=True)
			for m in models:
				path_full = os.path.join(path_base, m)
				if not os.path.isdir(path_full):
					Path(path_full).mkdir(parents=True, exist_ok=True)


def get_device():
	"""Check the device available on the current machine.
	Args:
		None.
	Returns:
		str: The device name.
	"""
	device = 'cpu'
	# Macos GPU
	#if torch.backends.mps.is_available():
	#	device = 'mps'
	# Cuda GPU
	if torch.cuda.is_available():
		device = 'cuda'
	return device


def write_dict_to_csv(file, my_dict):
	"""Write to csv file the given dictionary.
	Args:
		file (str): The file's path.
		my_dict (dict): Data to be written as a Python dictionary.
	Returns:
		None.
	
	if os.path.isfile(file):
		with open(file, 'a', encoding='utf-8') as outfile:
			csvwriter = csv.writer(outfile, delimiter=',')
			csvwriter.writerow(my_dict.values())
	else:"""
	with open(file, 'w', encoding='utf-8') as outfile:
			csvwriter = csv.writer(outfile, delimiter=',')
			csvwriter.writerow(my_dict)
			csvwriter.writerow(my_dict.values())


def get_date_time():
	"""Convert the current date in standard datetime format.
	Args:
		None.
	Returns:
		str: The datetime formatted.
	"""
	ts = datetime.timestamp(datetime.now())
	date_time = datetime.fromtimestamp(ts)
	return date_time.strftime("%Y-%m-%d %H:%M:%S")
