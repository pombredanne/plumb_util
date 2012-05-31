
from gevent import monkey; monkey.patch_all()
from IPython.frontend.terminal.ipapp import launch_new_instance

def gipython():
    launch_new_instance()
