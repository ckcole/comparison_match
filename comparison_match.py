class comparisonMatching:
    def __init__(self, it1, it2):
        self.it1 = it1
        self.val1 = self.it1.next()
        self.it2 = it2
        self.val2 = self.it2.next()
        self.output = []

    def next(self):
        # Returns an int if it can, or None
        if self.val1 > self.val2:
            self.val2 = self.it2.next()
        elif self.val1 < self.val2:
            self.val1 = self.it1.next()
        elif self.val1 == self.val2:
            match = self.val1
            self.val1 = self.it1.next()
            return match

    def has_next(self):
        #  Returns a bool.
        #  self.matched_val will be the self.val1 which will be equal to self.val2
        #  Calls itself recursively so that it will always be a bool
        #  Returns false when the iterators cant iterate any longer.
        try:
            self.matched_val = self.next()
            if self.matched_val:
                self.output.append(self.matched_val)
                return True
            else:
                return self.has_next()
        except StopIteration:
            return False


it1 = iter([1, 3, 5, 21, 25, 22])
it2 = iter([1, 5, 7, 10, 11, 52])

test = comparisonMatching(it1, it2)
hn = test.has_next()
while hn:
    print 'has_next: {}'.format(hn)
    hn = test.has_next()
print 'has_next: {}'.format(hn)
print test.output