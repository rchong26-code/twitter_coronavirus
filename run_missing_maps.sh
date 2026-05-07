#!/bin/bash

input_folder="/data/Twitter dataset"
output_folder="./outputs"

for file in "$input_folder"/geoTwitter20-*.zip
do
    base=$(basename "$file")

    if [ ! -f "$output_folder/$base.lang" ] || [ ! -f "$output_folder/$base.country" ]; then
        echo "Processing missing file: $file"
        nohup python3 src/map.py \
            --input_path "$file" \
            --output_folder "$output_folder" &
    fi
done

echo "All missing mapper jobs started"
