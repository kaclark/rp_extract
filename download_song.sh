#!/bin/sh
#output Path not tested, but method works
song_url=""
yt-dlp -x --audio-format wav $song_url -o ./songs/$1
