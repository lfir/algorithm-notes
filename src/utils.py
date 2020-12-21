def printNumTable(table):
    header = [''] + ['c' + str(x) for x in range(len(table[0]))]
    print('\t'.join([str(cell) for cell in header]))
    print('\n'.join(['\t'.join(['r' + str(i)] + [str(cell) for cell in row]) for i, row in enumerate(table)]))
