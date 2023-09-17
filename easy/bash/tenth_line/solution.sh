#!/usr/bin/env bash

# Given a text file file.txt, print just the 10th line of the file.

awk 'NR == 10 { print $0 }' file.txt
