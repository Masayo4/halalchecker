import os

def halal_checker_init():
    if os.path.exists('data.json') == True:
        os.remove('data.json')
