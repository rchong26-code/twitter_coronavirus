#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

OUTDIR="$(pwd)/outputs"
mkdir -p "$OUTDIR"
MAX_JOBS=8

for file in "/data/Twitter dataset"/geoTwitter20-*.zip; do
  base="$(basename "$file")"
  out="$OUTDIR/$base.country"
  log="$OUTDIR/$base.country.log"

  if [[ -s "$out" ]]; then
    echo "SKIP $base (country exists)"
    continue
  fi

  while (( $(pgrep -fc "python3 src/map.py") >= MAX_JOBS )); do
    sleep 2
  done

  echo "START $base"
  nohup python3 src/map.py --input_path "$file" --output_folder "$OUTDIR" > "$log" 2>&1 &
done

echo "All missing country jobs launched (throttled)."
