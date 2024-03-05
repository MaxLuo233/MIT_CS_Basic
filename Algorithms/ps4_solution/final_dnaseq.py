import unittest
from dnaseqlib import *

### Utility classes ###

class RollingHash:
    def __init__(self, s):
        self.HASH_BASE = 7
        self.seqlen = len(s)
        n = self.seqlen - 1
        h = 0
        for c in s:
            h += ord(c) * (self.HASH_BASE ** n)
            n -= 1
        self.curhash = h

    # Returns the current hash value.
    def hash(self):
        return self.curhash

    # Updates the hash by removing previtm and adding nextitm.  Returns the updated
    # hash value.
    def slide(self, previtm, nextitm):
        self.curhash = (self.curhash * self.HASH_BASE) + ord(nextitm)
        self.curhash -= ord(previtm) * (self.HASH_BASE ** self.seqlen)
        return self.curhash

class Multidict:
    def __init__(self, pairs=[]):
        self.table = dict()
        for pair in pairs:
            self.put(pair[0], pair[1])
    def put(self, k, v):
        if k in self.table:
            self.table[k].append(v)
        else:
            self.table[k] = [v]
    def get(self, k):
        try:
            return self.table[k]
        except KeyError:
            return []

"""间隔哈希"""
def getExactSubmatches(a, b, k, m):
    print ("Building table from sequence A...")
    seqtable = Multidict(intervalSubsequenceHashes(a, k, m))
    print ("...done building table.")
    for hashval, (bpos, bsubseq) in subsequenceHashes(b, k):
        for apos, asubseq in seqtable.get(hashval):
            if asubseq != bsubseq:
                continue
            yield (apos, bpos)
    return

def subsequenceHashes(seq, k):
    try:
        assert k > 0
        subseq = ''
        for i in range(0, k):
            subseq += seq.next()
        rh = RollingHash(subseq)
        pos = 0
        while True:
            yield (rh.hash(), (pos, subseq))
            previtm = subseq[0]
            subseq = subseq[1:] + seq.next()
            rh.slide(previtm, subseq[-1:])
            pos += 1
    except StopIteration:
        return

def intervalSubsequenceHashes(seq, k, m):
    assert m >= k
    try:
        pos = 0
        while True:
            subseq = ''
            for i in range(0, k):
                subseq += seq.next()
            rh = RollingHash(subseq)
            yield (rh.hash(), (pos, subseq))
            for i in range(0, m-k):
                seq.next()
            pos += m
    except StopIteration:
        return


class TestRollingHash(unittest.TestCase):
    def test_rolling(self):
        rh1 = RollingHash('abcde')
        rh2 = RollingHash('bcdef')
        rh3 = RollingHash('cdefZ')
        rh1.slide('a','f')
        self.assertTrue(rh1.hash() == rh2.hash())
        rh1.slide('b','Z')
        self.assertTrue(rh1.hash() == rh3.hash())

class TestMultidict(unittest.TestCase):
    def test_multi(self):
        foo = Multidict()
        foo.put(1, 'a')
        foo.put(2, 'b')
        foo.put(1, 'c')
        self.assertTrue(foo.get(1) == ['a','c'])
        self.assertTrue(foo.get(2) == ['b'])
        self.assertTrue(foo.get(3) == [])

# This test case may be useful before you add the argument m
# class TestExactSubmatches(unittest.TestCase):
#    def test_one(self):
#        foo = 'yabcabcabcz'
#        bar = 'xxabcxxxx'
#        matches = list(getExactSubmatches(iter(foo), iter(bar), 3, 4))
#        correct = [(1,2), (4,2), (7,2)]
#        self.assertTrue(len(matches) == len(correct))
#        for x in correct:
#            self.assertTrue(x in matches)

def compareSequences(afile, bfile, k, m):
    a = kfasta.FastaSequence(afile)
    b = kfasta.FastaSequence(bfile)
    matches = getExactSubmatches(a, b, k, m)
    with open('out1','w') as f:
        for match in matches:
            f.write(str(match)+'\n')

if __name__ == '__main__':
    # unittest.main()
    compareSequences('dist/data/fmaternal0.fa', 'dist/data/fpaternal0.fa', 8, 20)