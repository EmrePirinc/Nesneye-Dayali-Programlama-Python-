#15.Hafta Sorusu 
import datetime as dt
def yasGetir(tarih):
    tarih=dt.datetime.strptime(tarih,"%d/%m/%Y")
    fark=dt.datetime.now()-tarih
    yas=fark.days/365
    return yas




