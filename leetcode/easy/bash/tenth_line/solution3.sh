#!/usr/bin/env bash
# Given a text file file.txt, print just the 10th line of the file.

tail -n +10 file.txt | head -1
