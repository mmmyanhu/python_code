import operator , itertools

def accu(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total

# for a in accu([1,2,3,4,5]):
#     print(a)
a = (x for x in accu([1,2,3,4]))
b = (x for x in itertools.accumulate([1,2,3,]))
for m in a:
    print(m)