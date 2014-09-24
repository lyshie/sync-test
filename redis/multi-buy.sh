#!/bin/sh

# init
./clear.py

# exec
for i in $(seq 1 50); do
    delay=$( expr \( 50 - $i \) )
    { ./buy.py $i $delay; } &
done

# wait for all finished
wait

# show
./get.py
