#!/usr/bin/env python3

import argparse
import os
import zipfile
import datetime
import json
from collections import Counter, defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--input_path', required=True)
parser.add_argument('--output_folder', default='outputs')
args = parser.parse_args()

hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
]

hashtags_lower = [h.lower() for h in hashtags]

counter_lang = defaultdict(Counter)
counter_country = defaultdict(Counter)

def get_lang(tweet):
    lang = tweet.get('lang')
    return lang if lang else 'und'

def get_country(tweet):
    place = tweet.get('place')
    if isinstance(place, dict):
        cc = place.get('country_code') or place.get('country')
        if cc:
            return cc
    return '??'

with zipfile.ZipFile(args.input_path) as archive:
    for filename in archive.namelist():
        print(datetime.datetime.now(), args.input_path, filename)

        with archive.open(filename) as f:
            for raw_line in f:
                try:
                    tweet = json.loads(raw_line)
                except Exception:
                    continue

                text = tweet.get('text', '')
                if not isinstance(text, str):
                    continue
                text_lower = text.lower()

                lang = get_lang(tweet)
                country = get_country(tweet)

                counter_lang['_all'][lang] += 1
                counter_country['_all'][country] += 1

                for h, hlow in zip(hashtags, hashtags_lower):
                    if hlow in text_lower:
                        counter_lang[h][lang] += 1
                        counter_country[h][country] += 1

os.makedirs(args.output_folder, exist_ok=True)
output_base = os.path.join(args.output_folder, os.path.basename(args.input_path))

out_lang = output_base + '.lang'
print('saving', out_lang)
with open(out_lang, 'w') as f:
    f.write(json.dumps({k: dict(v) for k, v in counter_lang.items()}))

out_country = output_base + '.country'
print('saving', out_country)
with open(out_country, 'w') as f:
    f.write(json.dumps({k: dict(v) for k, v in counter_country.items()}))

