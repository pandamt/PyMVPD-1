import os

# helper function to determine mvpd directory path
def get_mvpd_directory():
    return os.path.dirname(os.path.abspath(__file__))
