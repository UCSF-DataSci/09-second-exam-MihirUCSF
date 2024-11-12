#!/bin/bash

# Step 1: Run the script to generate dirty data
python "C:/Users/mihir/OneDrive/Desktop/Assignment9/generate_dirty_data.py"

# Step 2: Clean the data
# Remove comment lines, empty lines, and extra commas
grep -v '^#' "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data_dirty.csv" | sed '/^$/d' | sed 's/,,*/,/g' > "C:/Users/mihir/OneDrive/Desktop/Assignment9/temp.csv"

# Extract essential columns and filter walking speeds
awk -F, 'BEGIN {OFS=","} {if ($6 >= 2.0 && $6 <= 8.0) print $1, $2, $4, $5, $6}' "C:/Users/mihir/OneDrive/Desktop/Assignment9/temp.csv" > "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv"

# Step 3: Create insurance.lst with unique insurance types
echo -e "insurance_type\nBasic\nPremium\nPlatinum" > "C:/Users/mihir/OneDrive/Desktop/Assignment9/insurance.lst"

# Step 4: Generate a summary of the processed data
# Count the total number of visits
total_visits=$(wc -l < "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv")
total_visits=$((total_visits - 1)) # Subtract header row

# Display the first few records
head -n 5 "C:/Users/mihir/OneDrive/Desktop/Assignment9/ms_data.csv"

# Output the total number of visits
echo "Total number of visits: $total_visits"

# Clean up temporary file
rm "C:/Users/mihir/OneDrive/Desktop/Assignment9/temp.csv"