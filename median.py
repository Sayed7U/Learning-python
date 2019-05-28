__author__ = 'Sayed'


def median(List):
    if len(List) > 1:
        midele = float(len(List) + 1)/ float(2)
        List = sorted(List)
        if len(List) % 2 == 0:
            median = float((List[int(midele - 1)] + List[int(midele)]))  / float(2)
        else:
            median = List[int(midele-1)]
        print(List)
        print(median)
    else:
        print(List[0])
while True:
    a = [int(x) for x in input("Enter input:").split()]
    median(a)

