#!/bin/bash

# dataset location
input_folder="/data/Twitter dataset"

# where outputs go
output_folder="./outputs"

# loop over 2020 tweets
for file in "$input_folder"/geoTwitter20-*.zip
do
    echo "Processing $file"

    nohup python3 src/map.py \
        --input_path "$file" \
        --output_folder "$output_folder" &
done

echo "All mapper jobs started"

