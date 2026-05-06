import os
os.system("cls")

#1.m 
import datetime

# hozirgivaqt=datetime.datetime.now()
# print(hozirgivaqt)


# 2.m
# yil=int(input("Yil- "))
# oy=int(input("oy- "))
# kun=int(input("kun- "))
# if yil>0 and oy>0 and kun>0 and yil<=2026 and oy<14 and kun<32:
#     tugilganyili=datetime.date(yil,oy,kun)
#     hozirgivaqt=datetime.date.today()
#     qancha_kun_korgan=hozirgivaqt-tugilganyili
#     print(qancha_kun_korgan.days)
# else:
#     print("Iltimos to'g'ri kunlarni kiriting")


# 3.m
# def vaqt(a):
#     bayram=datetime.date(2026,9,1)
#     bugun=datetime.date.today()
#     print(bayram-bugun)
#     print(a)

# vaqt("Bayramga oz qoldi")


# 4.m
# A=[
#     [1,2],
#     [3,4]
# ]
# B=[
#     [5,6],
#     [7,8]
# ]
# C=[
#     [0,0],
#     [0,0]
# ]
# for i in range(len(A)):
#     C[i]=[A[i][0]+B[i][0],A[i][1]+B[i][1]]

# print(C)


# 5.m
# from translate import Translator
# tarjimon=Translator(to_lang="en",from_lang="uz")
# list1=["Salom", "dastur", "yordam",  "kitob"]
# dict1={}
# for soz in list1:
    
#     dict1[soz]=tarjimon.translate(soz)

# for i,j in dict1.items():
#     print(f"{i}:{j}")


# 6.m
filmlar = {
    "Titanic": "Jack Dawson",
    "Harry Potter": "Harry Potter",
    "The Dark Knight": "Bruce Wayne (Batman)",
    "The Matrix": "Neo (Thomas Anderson)",
    "Forrest Gump": "Forrest Gump",
    "Gladiator": "Maximus Decimus Meridius",
    "Inception": "Dom Cobb",
    "Spider-Man": "Peter Parker",
    "Iron Man": "Tony Stark",
    "The Lord of the Rings": "Frodo Baggins"
}

try:
    f_nomi=input("")
    for kino,aktyor in filmlar.items():
        if f_nomi==kino:
            print(aktyor)
except KeyError:
    print("Bunday film yo'q!")



