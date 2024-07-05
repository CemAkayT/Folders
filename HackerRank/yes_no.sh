#!/usr/local/bin/bash

read -r X

if [[ "${X,}" == 'n' ]]; then
    echo "NO"
else
    echo "YES"
fi
