#!/bin/bash

tmux new-session -d -s my_session

tmux split-window -h

tmux send-keys -t my_session:0.0 'clear && time python concurrency.py' C-m

tmux send-keys -t my_session:0.1 'clear && time python gb_coroutine.py' C-m

tmux attach -t my_session
