#!/bin/sh

# init
rm -f /tmp/count
touch /tmp/count

# exec
for i in $(seq 1 100); do
    delay=$(expr \( 100 - $i \) \* 1000 )
    { ./flock.pl $i $delay; } &
done

# wait for all finished
wait

# show
echo -n "["
cat /tmp/count
echo -n "]"
