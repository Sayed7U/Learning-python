__author__ = 'Sayed'


def median(l):
    if len(l) > 1:
        midele = float(len(l) + 1)/ float(2)
        l = sorted(l)
        if len(l) % 2 == 0:
            median = float((l[int(midele - 1)] + l[int(midele)]))  / float(2)
        else:
            median = l[int(midele - 1)]
        return median
    else:
        return l[0]

