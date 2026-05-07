#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--output_path', required=True)
args = parser.parse_args()

# imports
import json
from collections import Counter, defaultdict

# load each of the input paths
total = defaultdict(lambda: Counter())

for path in args.input_paths:
    try:
        with open(path) as f:
            tmp = json.load(f)

        for k in tmp:
            total[k] += Counter(tmp[k])

    except json.JSONDecodeError:
        print(f"Skipping invalid JSON file: {path}")
    except Exception as e:
        print(f"Skipping {path}: {e}")

# write the output path
with open(args.output_path, 'w') as f:
    json.dump(total, f)
