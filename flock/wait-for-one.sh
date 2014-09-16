#!/bin/sh

# init
rm -f /tmp/count
touch /tmp/count

# exec
{ ./flock.pl 1 2000000; } &

# add a delay to ensure that job-1 runs before job-2
sleep 0.1

{ ./flock.pl 2 0; } &

# wait for all finished
wait

# show
echo -n "["
cat /tmp/count
echo -n "]"
