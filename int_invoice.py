import csv

data_file = 'data1.txt'
# добовление данных из файл 
def insert_data(num_ip):
    tmp1 = []  # list
    tmp2 = []
    with open(data_file,'r') as csvfile:
        csvreader = csv.reader(csvfile)
        tmp1 = csvreader.__next__()
        for row in csvreader:
            tmp2.append(row)
    res = []
    for row in tmp2:
        string = row[0].split()[0] # split - method splits a string into a list.
        if string == num_ip:
            res.append(row)
    return tmp1,res