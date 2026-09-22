#!/bin/bash
set -euo pipefail
INPUT="lab3_data.tsv"
CLEANED="cleaned.tsv"
CSV="converted.csv"

curl -sL -o lab3-bundle.tar.gz https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' "$INPUT" > "$CLEANED"
tr '\t' ',' < "$CLEANED" > "$CSV"
DATA_ROWS=$(tail -n +2 "$CSV" | wc -l | tr -d ' ')
echo "Number of data rows: ${DATA_ROWS}"
tar -czf converted-archive.tar.gz "$CSV"