#!/bin/bash

# Run script to generate dirty data
python "C:/Users/mihir/OneDrive/Desktop/Assignment9/generate_dirty_data.py"

# Clean the raw data file
grep -v '^#' "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data_dirty.csv" | \
sed '/^$/d' | \
sed 's/,,*/,/g' | \
awk -F, 'BEGIN {OFS=","} {print $1, $2, $4, $5, $6}' | \
awk -F, '$5 >= 2.0 && $5 <= 8.0' > "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv"

# Create insurance.lst file
echo "Basic" > "C:/Users/mihir/OneDrive/Desktop/Assignment9/insurance.lst"
echo "Premium" >> "C:/Users/mihir/OneDrive/Desktop/Assignment9/insurance.lst"
echo "Platinum" >> "C:/Users/mihir/OneDrive/Desktop/Assignment9/insurance.lst"

# Generate Summary
total_visits=$(wc -l < "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv")
echo "Total number of visits (excluding header): $((total_visits - 1))"
echo "First few records:"
head -n 5 "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv"
