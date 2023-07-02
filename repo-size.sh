#!/bin/bash

magnitudes=(K M G T P E Z)

if [ -z $1 ]; then
    echo "repository not specified"
    exit 1
fi

size=$(curl -s https://api.github.com/repos/$1 | grep size | awk '{print $2}' | tr -d ',')

if [ -z $size ]; then
    echo "repository not found"
    exit 1
fi

for i in "${!magnitudes[@]}"; do
    if (($size < 1000)); then
        echo "$size ${magnitudes[i]}B"
        exit 0
    fi

    size=$((size / 1000))
done
