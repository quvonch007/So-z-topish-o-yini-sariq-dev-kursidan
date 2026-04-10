import random as r

def son_top(son):
    '''Bu funksiya o'zi son o'ylaydi va biz uni topishga harakat qilamiz'''
    urinishlar = 1
    tahmin_son = r.randint(1,son)

    user = float(input(f"1 dan {son} gacha son o'yladim. Toping: "))

    while user != tahmin_son:
        urinishlar += 1
        if user < tahmin_son:
            print("Men kattaroq son o'ylagan edim")
        else:
            print("Men kichikroq son o'ylagan edim") 

        user = int(input("Yana urinib ko'ring: "))

    #Sikldan chiqdi degani - sonni topdi degani
    print(f"Tabriklaymiz! Siz {urinishlar} ta urinishda topdingiz!")
    return urinishlar


def sonimni_top(son):
    print(f'1 dan {son} gacha son o\'ylang, men topishga harakat qilaman')
    quyi = 1
    yuqori = son
    urinishlar = 0

    while True:
        urinishlar += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi 

        javob = input(f"Siz {taxmin} soni o'yladingiz. To'g'ri (t),\n"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-): ").lower()
        
        if javob == '-':
            yuqori = taxmin - 1
        elif javob == '+':
            quyi = taxmin + 1
        elif javob == 't':
            print(f"Urra! Men {urinishlar} ta urinish bilan topdim!")
            break
    return urinishlar

