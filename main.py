from threading import *

from terminal import *
import listener

cmd = ''

if __name__ == '__main__':
    #terminal
    terminal = Terminal()
    terminal_thread = Thread(target=terminal.cmdloop)
    terminal_thread.start()
    #web
    print('Starting Webserver')
    listener.run()