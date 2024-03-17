#!/$PREFIX/bin/bash

import sys
from sh import termux_clipboard_get
from sh import termux_clipboard_set
print("Termux is pulling from clipboard")
raw = str(termux_clipboard_get())
formatted1= raw.replace("\r"," ")
formatted2 = formatted1.replace("\n"," ")
print("raw data is unchanged", raw == formatted2)
termux_clipboard_set(formatted2)
print("clipboard should now be set")
