#!/usr/local/bin/bash

    read number

    sum=0
    for ((i=0; i<$number; i++)); do
        read input
        sum=$((sum + input))
    done

    avg=$(echo "scale=4; $sum / $number" | bc)

    echo $(printf "%.3f" "$avg")



