import json
import time
class Kitob:
    def __init__(self, nomi, muallifi, janri, narxi, mavjud=True, ijarada=False):
        self.nomi = nomi
        self.muallifi = muallifi
        self.janri = janri
        self.narxi = narxi
        self.mavjud = mavjud
        self.ijarada = ijarada

    def to_dict(self):
        return {
            "nomi": self.nomi,
            "muallifi": self.muallifi,
            "janri": self.janri,
            "narxi": self.narxi,
            "mavjud": self.mavjud,
            "ijarada": self.ijarada
        }



class Foydalanuvchi:
    def __init__(self, ism, login, parol):
        self.ism = ism
        self.login = login
        self.parol = parol



    def to_dict(self):
        return {
            "ism": self.ism,
            "login": self.login,
            "parol": self.parol
        }
    



class Kutubxona:
    def __init__(self):
        self.kitoblar = []
        self.foydalanuvchilar = []




    def kitob_qoshish(self, kitob):
        self.kitoblarni_yuklash() 
        self.kitoblar.append(kitob)
        self.kitoblarni_saqlash()  



    def kitoblarni_saqlash(self, fayl_nomi="kitob.json"):
        kitoblar_dict = [kitob.to_dict() for kitob in self.kitoblar]
        with open(fayl_nomi, 'w') as fayl:
            json.dump(kitoblar_dict, fayl, ensure_ascii=False, indent=4)





    def kitoblarni_yuklash(self, fayl_nomi="kitob.json"):
        try:
            with open(fayl_nomi, 'r') as fayl:
                kitoblar_dict = json.load(fayl)
                self.kitoblar = [Kitob(**kitob) for kitob in kitoblar_dict]
        except FileNotFoundError:
            print(f"{fayl_nomi} fayli topilmadi!")




    def kitobni_qidirish(self, kitob_nomi):
        self.kitoblarni_yuklash()  
        for kitob in self.kitoblar:
            if kitob.nomi.lower() == kitob_nomi.lower():
                time.sleep(1)
                return f"Kitob topildi: {kitob.nomi}, Muallif: {kitob.muallifi}, Janr: {kitob.janri}, Narx: {kitob.narxi} so'm"
        return "Bunday kitob topilmadi."




    def foydalanuvchi_royxatdan_otish(self, foydalanuvchi):
        for foydalanuvchi_obj in self.foydalanuvchilar:
            if foydalanuvchi_obj.login == foydalanuvchi.login:
                return "Bunday login mavjud, boshqa login tanlang."
        self.foydalanuvchilar.append(foydalanuvchi)
        self.foydalanuvchilarni_saqlash()
        return f"Foydalanuvchi ro'yxatdan o'tdi: {foydalanuvchi.ism}"
    

    

    def foydalanuvchi_tizimga_kirish(self, login, parol):
        for foydalanuvchi in self.foydalanuvchilar:
            if foydalanuvchi.login == login and foydalanuvchi.parol == parol:
                return f"Xush kelibsiz, {foydalanuvchi.ism}!"
        return "Login yoki parol xato!"





    def foydalanuvchilarni_saqlash(self, fayl_nomi="foydalanuvchilar.json"):
        foydalanuvchilar_dict = [foydalanuvchi.to_dict() for foydalanuvchi in self.foydalanuvchilar]
        with open(fayl_nomi, 'w') as fayl:
            json.dump(foydalanuvchilar_dict, fayl, ensure_ascii=False, indent=4)




    def foydalanuvchilarni_yuklash(self, fayl_nomi="foydalanuvchilar.json"):
        try:
            with open(fayl_nomi, 'r') as fayl:
                foydalanuvchilar_dict = json.load(fayl)
                self.foydalanuvchilar = [Foydalanuvchi(**foydalanuvchi) for foydalanuvchi in foydalanuvchilar_dict]
        except FileNotFoundError:
            print(f"{fayl_nomi} fayli topilmadi!")
    

    def kitob_ijaraga_olish(self, kitob_nomi):
            self.kitoblarni_yuklash()
            for kitob in self.kitoblar:
                if kitob.nomi.lower() == kitob_nomi.lower():
                    if kitob.mavjud:
                        kitob.mavjud = False
                        kitob.ijarada = True
                        self.kitoblarni_saqlash()
                        return f"Kitob ijaraga olindi: {kitob.nomi}"
                    else:
                        return "Kitob allaqachon ijarada."
            return "Bunday kitob topilmadi."

    def kitob_qaytarish(self, kitob_nomi):
        self.kitoblarni_yuklash()
        for kitob in self.kitoblar:
            if kitob.nomi.lower() == kitob_nomi.lower() and kitob.ijarada:
                kitob.mavjud = True
                kitob.ijarada = False
                self.kitoblarni_saqlash()
                return f"Kitob qaytarildi: {kitob.nomi}"
        return "Bunday kitob ijarada emas yoki topilmadi."




    def kitoblar_royxati(self):
        self.kitoblarni_yuklash()
        if self.kitoblar:
            print("Kutubxonadagi kitoblar:")
            for kitob in self.kitoblar:
                holat = "Ijarada" if kitob.ijarada else "Mavjud"
                print(f"  {kitob.nomi} - {holat}")
        else:
            print("Kutubxonada kitoblar yo'q.")

    def ijaradagi_kitoblar_royxati(self):
        self.kitoblarni_yuklash()
        ijaradagi_kitoblar = [kitob for kitob in self.kitoblar if kitob.ijarada]
        if ijaradagi_kitoblar:
            print("Ijaraga olingan kitoblar:")
            for kitob in ijaradagi_kitoblar:
                print(f"  {kitob.nomi}")
        else:
            print("Ijaraga olingan kitoblar yo'q.")






kutubxona = Kutubxona()
kutubxona.foydalanuvchilarni_yuklash("foydalanuvchilar.json")

