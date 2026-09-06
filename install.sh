#!/usr/bin/bash

while read package
do
   pkg install "$package" -y
done < packages.txt

