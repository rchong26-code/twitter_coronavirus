#!/usr/bin/env python3

import argparse
import glob
import os
import json
import datetime

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


def day_from_filename(path):
    base = os.path.basename(path)
    date_part = base.split(".zip")[0].replace("geoTwitter", "")
    return datetime.datetime.strptime(date_part, "%y-%m-%d").date()


parser = argparse.ArgumentParser()
parser.add_argument("hashtags", nargs="+")
parser.add_argument("--glob", default="outputs/geoTwitter20-*.zip.lang")
parser.add_argument("--out", default="plots/hashtag_timeseries.png")
args = parser.parse_args()

paths = sorted(glob.glob(args.glob))
if not paths:
    raise SystemExit("No daily files found")

dates = [day_from_filename(p) for p in paths]

series = {h: [] for h in args.hashtags}

for p in paths:
    with open(p) as f:
        counts = json.load(f)

    for h in args.hashtags:
        d = counts.get(h, {})
        if isinstance(d, dict):
            series[h].append(sum(d.values()))
        else:
            series[h].append(0)

os.makedirs(os.path.dirname(args.out), exist_ok=True)

plt.figure(figsize=(11,6))

for h in args.hashtags:
    plt.plot(dates, series[h], linewidth=2, label=h)

plt.xlabel("Day of year (2020)")
plt.ylabel("Tweet count")

ax = plt.gca()
ax.set_yscale("log")
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda y, _: f"{int(y):,}" if y >= 1 else "0"))
ax.yaxis.set_minor_formatter(mtick.NullFormatter())

plt.legend()
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(args.out, dpi=200)
print("saved", args.out)
