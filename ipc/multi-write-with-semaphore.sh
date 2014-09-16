#!/bin/sh

# init
rm -f /tmp/count
touch /tmp/count

# destroy the semaphore first
./clear.py

# exec
for i in $(seq 1 100); do
    { ./inc_with_semaphore.py $i $delay; } &
done

# wait for all finished
wait

# show
echo -n "["
cat /tmp/count
echo -n "]"
