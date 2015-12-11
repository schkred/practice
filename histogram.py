__author__ = 'Schkred'
seq = [3, 5, 8, 13]
def histo(sequence) :
    i = max(sequence)
    while i >= 1 :
        tmp = ''
        for x in seq :
            if x >= i :
                tmp +=' * '
            else :
               tmp +='   '
        print tmp
        i -= 1

histo(seq)