HOW TO RUN:

To use cmu_112_graphics.py, you need to have some modules installed. If they are
not installed, you will see a message like this (or a similar one for "requests" instead of "PIL"):

---

** Cannot import PIL -- it seems you need to install pillow
** This may result in limited functionality or even a runtime error.

---

You can try to use 'pip' to install the missing modules, but it can be complicated
making sure you are installing these modules for the same version of Python that you are running. Here are some more-reliable steps that should work for you:

For Windows:
Run this Python code block in a Python file (it will print the commands you need to paste into your command prompt):

import sys
print(f'"{sys.executable}" -m pip install pillow')
print(f'"{sys.executable}" -m pip install requests')

Open Command Prompt as an administrator user (right click - run as administrator)
Copy-paste each of the two commands printed in step 1 into the command prompt you opened in step 2.
Close the command prompt and close Python.
Re-open Python, and you're set (hopefully)!

For Mac or Linux:
Run this Python code block in a Python file (it will print the commands you need to paste into your command prompt):

import sys
print(f'sudo "{sys.executable}" -m pip install pillow')
print(f'sudo "{sys.executable}" -m pip install requests')

Open Terminal
Copy-paste each of the two commands printed in step 1 into the command prompt you opened in step 2.
If you see a lock and a password is requested, type in the same password that you use to log into your computer.
Close the terminal and close Python.
Re-open Python, and you're set (hopefully)!

Now all you need to have this folder, go to snake.py and run that file.

HOW TO PLAY:

Press R to restart
