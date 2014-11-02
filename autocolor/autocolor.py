from hashlib import sha1
import re


class AutoColor(object):

    def __init__(self, label):
        self.label = label
        self.hash = sha1(self.label).hexdigest()[:6]

    def hex(self):
        return '#%s' % self.hash.upper()

    def rgb(self):
        return tuple(int(x, 16) for x in re.findall('.{2}', self.hash))
