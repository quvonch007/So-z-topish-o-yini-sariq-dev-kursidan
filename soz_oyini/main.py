import funksiyalar as fk

print('Keling bir o\'yin o\'ynaylik')



def hisob():
    
    while True:
        qaytgan = input("O'yin o'ynasangiz yes/no: ")

        if qaytgan == 'yes':
            start = fk.son_top(10) # kompyuter 10gacha son o'ylaydi
            second = fk.sonimni_top(10)
            if start < second:
                print(f"Siz yutdingiz! {start} urinish bilan")
            elif start > second:
                print(f"Men yutdim! {second} urinish bilan")
            elif start == second:
                print("Durrang bo'ldi!")
        else:
            print("O'yin tugadi!")
            break

hisob()

