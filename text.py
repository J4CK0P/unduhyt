import random
import sys
import time
def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
type('Anjing Kau || Bangsat Kau - J4CKOP.')
