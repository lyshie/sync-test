#!/bin/sh

# init
( ./server.py & )

sleep 1
echo "Wait for 2 seconds to start clients..."
sleep 2

# exec
for i in $(seq 1 30); do
    { ./client_lock.py; } &
done

# wait for all finished
wait

# shutdown the server
PID=$(pgrep -f ./server.py)
kill -s INT ${PID}
