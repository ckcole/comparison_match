it1 = iter([1,3,5,21,25,22])
it2 = iter([1,5,7,10,11,52])


class comparisonMatching:
    def __init__(self, it1, it2):
        self.it1 = it1
        self.val1 = self.it1.next()
        self.it2 = it2
        self.val2 = self.it2.next()
        self.output = []

    def next(self):
        if self.val1 > self.val2:
            print 'gt'
            self.val2 = self.it2.next()
        elif self.val1 < self.val2:
            print 'lt'
            print 'val1 {}'.format( self.val1)
            self.val1 = self.it1.next()
        elif self.val1 == self.val2:
            print 'match'
            match = self.val1
            self.val1 = self.it1.next()
            return match
        else:
            print 'None'

    def has_next(self):
        try:
            self.matched_val = self.next()
            if self.matched_val:
                self.output.append(self.matched_val)
            else:
                self.has_next()
            return True  
        except StopIteration:
            return False


test = comparisonMatching(it1, it2)
hn = test.has_next()
while hn:
    print 'has_next: {}'.format(hn)
    hn = test.has_next()
print 'has_next: {}'.format(hn)
print test.output