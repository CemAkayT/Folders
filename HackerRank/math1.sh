#!/usr/local/bin/bash


echo "Enter a mathematical expression:"
read expression

# Using bc to evaluate the expression with scale set to 4
result=$(echo "scale=3; $expression" | bc)

# Using printf to round the result to 3 decimal places
rounded_result=$(printf "%.3f" "$result")

echo "$rounded_result"

