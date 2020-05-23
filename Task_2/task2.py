import csv


def csvReaderInit(fileObj, map):
    reader = csv.DictReader(fileObj, delimiter=';')
    for line in reader:
        map[line.get('PROD_CODE')] = list()


def csvReader(fileObj, map):
    reader = csv.DictReader(fileObj, delimiter=';')
    for line in reader:
        prodCode = line.get('PROD_CODE')
        basket = line.get('BASKET_ID')
        map[prodCode] = list(map.get(prodCode)).append(basket)


def main(map):
    file = 'transactions.csv'
    with open(file, "r") as fileObj:
        csvReaderInit(fileObj, map)
    with open(file, "r") as fileObj:
        csvReader(fileObj, map)
    print(map.values())


# Start
map = {}
main(map)
# End
