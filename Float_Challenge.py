import collections
population_dict = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates_country-1km-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = float(line[5])
        line[6] = float(line[6])
        if line[6] == 'Total National Population':
            population_dict[line[0]] += float(line[6] - line[5])

with open('national_population.csv', 'w') as outputFile:
    outputFile.write('continent,change_population\n')

    for k, v in population_dict.iteritems():
        outputFile.write(k + ',' + str(v) + '\n')
