"""
code test for ttl and key .
"""
from time import time, sleep
import itertools
from threading import Thread, RLock
import signal


"""
This code test for ttl and key CacheEntry class.
"""
class CacheEntry:

    def __init__(self, string, ttl=30):
        self.string = string
        self.expires_at = time() + ttl
        self._expired = False

    def expired(self):
        if self._expired is False:
            return self.expires_at < time()
        else:
            return self._expired


"""
code test for ttl and key CacheList class.
"""
class CacheList:

    def __init__(self):
        self.entries = []
        self.lock = RLock()

    def add_entry(self, string, ttl=30):
        with self.lock:
            self.entries.append(CacheEntry(string, ttl))

    def read_entries(self):
        with self.lock:
            self.entries = list(itertools.dropwhile(lambda x: \
                                x.expired(), self.entries))
            return self.entries

    def read_entries(name, slp, cachelist):
        while True:
            print '{}: {}'.format(name, ','.join(map(lambda x: \
                                  x.string, cachelist.read_entries())))
            sleep(slp)

    def add_entries(name, ttl, cachelist):
        str1 = 'O'
        while True:
            cachelist.add_entry(str1, ttl)
            print 'Added ({}): {}'.format(name, str1)
            sleep(1)
            str1 += 'O'

    if __name__ == '__main__':
        signal.signal(signal.SIGINT, signal.SIG_DFL)

        cl = CacheList()
        print_threads = []
        print_threads.append(Thread(None, read_entries, args=('t1', 1, cl)))
        adder_thread = Thread(None, add_entries, args=('a1', 2, cl))
        adder_thread.start()

    for t in print_threads:
        t.start()

    for t in print_threads:
        t.join()
