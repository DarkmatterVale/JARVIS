import sys
import subprocess
import os

# NOTE: Currently, only CLI will be implemented so STT engines and other class initialization will not be required

# Throughout the code in the main program, the following needs to be accomplished:
# 1: Initialize brain and other classes. This will allow JARVIS to interpret commands and access STT associated functions
# 2: In an infinite loop:
#   a: Get user input
#   b: Parse that user input for set commands such as shutdown, restart, etc
#   c: Compare that input to previous input/database of phrases and words and apply learning logic (see logic_basic_learning.txt)
