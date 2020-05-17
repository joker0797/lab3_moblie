import csv
dataFile = 'data.csv'
def insertData(phoneNum):
    fiels = []
    rows = []
    with open(dataFile,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fiels = csvreader.__next__()
        for row in csvreader:
            rows.append(row)
        # numRow = csvreader.line_num
    index1 = fiels.index('msisdn_origin')
    index2 = fiels.index('msisdn_dest')
    res = []
    for row in rows:
        if (row[index1] == phoneNum) or (row[index2] == phoneNum):
            res.append(row)
    return fiels,res