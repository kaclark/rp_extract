#!/bin/sh
#output Path not tested, but method works
song_url=$1
song_path=$2
yt-dlp -x --audio-format wav $song_url -o ./songs/$song_path
