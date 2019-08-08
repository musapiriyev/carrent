ct=input("Hansi tarifde gotureceynizi yazin .... :")
gun=int(input("Nece gunluk gotureceksiniz?...:"))
ilki_mil=int(input("Ilk mile qeyd edin..."))
son_mil=int(input("Son mile qeyd edin ..."))
borc=0
gedilen=son_mil-ilki_mil
if ct=="b":
    borc+=gun*40+gedilen*0.25
    print("Sizin gundelik ve mile gore borcunuz :",borc,"$")
elif ct=="d":
    if gedilen<100:
            borc+=gun*60
            print("Sizin gundeliy borcunuz",borc,"$")
    elif gedilen>100:
            borc+=gun*60+gedilen*0.25
            print("sizin gundeliy ve mil borcunuz:",borc,"$")
elif ct=="w":
    if gedilen<900:
        borc+=gun*190
        print("Sizin heftelik borcunuz",borc,"$")
    elif gedilen>900 and gedilen<1500:
        borc+=gun*(190+100)
        print("sizin gundeliy ve mil borcunuz:",borc,"$")
    elif gedilen>1500:
        borc+=gun*(190+200)+gedilen*0.25
        print("sizin heftelik borcunuz:",borc,"$")
   