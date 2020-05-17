import phone_invoice
def invoices(phoneNum):
    fiels,data = phone_invoice.insertData(phoneNum)
    origin = fiels.index('msisdn_origin')
    dest = fiels.index('msisdn_dest')
    call = fiels.index('call_duration')
    sms = fiels.index('sms_number')
    call_out_coef = 2 # //2руб/минута исходящие звонки,
    call_in_coef = 1 # //0руб/минута входящие первые 50 минут, далее 1руб/минута, 
    call_in_free = 50
    call_in_duration = 0
    call_out_duration = 0
    sms_number = 0
    sms_coef =1 
    for row in data:
        if row[origin] == phoneNum:
            call_out_duration += float(row[call])
            sms_number += float(row[sms])
        if row[dest] == phoneNum:
            call_in_duration += float(row[call])
    call_invoices = max(0,(call_in_duration-call_in_free)) *call_in_coef + call_out_coef*call_out_duration
    sms_invoices = sms * sms_coef
    return call_invoices+sms_invoices
