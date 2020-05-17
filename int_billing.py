import int_invoice
 #Протарифицировать трафик
def invoices(num_ip):
    _,data = int_invoice.insert_data(num_ip)
    sour = 0 # источник 
    dst = 1  # target 
    byte = 2
    
    k = 1 # коэффициентом k: 1руб/Мб 
    total = 0
    for row in data:
        a = row[sour].split()[0]
        if a == num_ip:
            b = row[dst].split()[0]
            c = row[byte].split()[0]
            total += float(c)


    total /= pow(2,20)
    internet_bill = total * k
    internet_bill = total
    return internet_bill