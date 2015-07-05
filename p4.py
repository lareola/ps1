
def tgb():
    for x in ['ten', 'nine', 'eight', 'seven', 'six', 'five', 'four', 'tree', 'two', 'one']:
        print x, " green bottles hanging on the wall,"
        print x, " green bottles hanging on the wall,"
        print "And if one green bottle should accidentally fall"
        if x == 'one':
            print "There'll be no green bottles hanging on the wall."
            break
        print "There'll be ", x, "green bottles hanging on the wall."


tgb()

