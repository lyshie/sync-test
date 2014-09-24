#!/bin/sh

# init
./clear.py

# exec
for i in $(seq 1 200); do
    delay=$( expr \( 200 - $i \) )
    { ./buy.py $i $delay; } &
done

# wait for all finished
wait

# show
./get.py
