#!/bin/sh

# exec
for i in $(seq 1 20); do
    delay=$( expr \( 20 - $i \) )
    { ./thread.py "sync"; } &
done

# wait for all finished
wait
