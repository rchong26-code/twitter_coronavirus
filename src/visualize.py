#!/usr/bin/env python3

import argparse
import os
import json
import urllib.parse

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--key', required=True)
parser.add_argument('--percent', action='store_true')
parser.add_argument('--outdir', default='plots')
parser.add_argument('--topk', type=int, default=10)
args = parser.parse_args()

with open(args.input_path) as f:
    counts = json.load(f)

if args.key not in counts:
    raise SystemExit(f"Key {args.key} not found")

if args.percent:
    series = {}
    for g,v in counts[args.key].items():
        denom = counts.get('_all',{}).get(g,0)
        if denom:
            series[g]=v/denom
else:
    series = counts[args.key]

top_items = sorted(series.items(), key=lambda kv:(kv[1],kv[0]), reverse=True)[:args.topk]
top_items = sorted(top_items, key=lambda kv:(kv[1],kv[0]))

labels=[k for k,_ in top_items]
values=[v for _,v in top_items]

os.makedirs(args.outdir,exist_ok=True)
safe_key=urllib.parse.quote(args.key,safe='')
base=os.path.basename(args.input_path)
suffix="percent" if args.percent else "count"
outpath=os.path.join(args.outdir,f"{base}__{safe_key}__{suffix}.png")

plt.figure(figsize=(10,6))
plt.bar(labels,values)
plt.xticks(rotation=45,ha='right')
plt.tight_layout()
plt.savefig(outpath,dpi=200)
print("saved",outpath)
