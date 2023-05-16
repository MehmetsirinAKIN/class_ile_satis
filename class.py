class Magaza:
    def __init__(self, magaza_adi="Bilinmiyor", Calisanlar=None):
        self.__magaza_adi = magaza_adi
        self.Calisanlar = [] if Calisanlar is None else Calisanlar

    def get_magaza_adi(self):
        return self.__magaza_adi

    def __str__(self):
        return f"Magaza Adi: {self.get_magaza_adi()}\t Magaza Toplam Satis: {str(self.magaza_satis_tutar())}"

    def calisanEkle(self,caliasan):
        self.Calisanlar.append(caliasan)

    def magazaBilgileri(self):
        print(self)
        for calisan in self.Calisanlar:
            print(calisan)

    def magaza_satis_tutar(self):
        toplamSatis = 0
        for calisan in self.Calisanlar:
            toplamSatis += calisan.satislariTopla()
        return toplamSatis

class Calisan:
    def __init__(self, satici_adi="Bilinmiyor", Satislar=[]):
        self.__satici_adi = satici_adi
        self.Satislar = [] if Satislar is None else Satislar

    def get_satici_adi(self):
        return self.__satici_adi

    def satisEkle(self, satis):
        self.Satislar.append(satis)

    def satislariListele(self):
        print(self)
        for satis in self.Satislar:
            print(satis)

    def satislariTopla(self):
        toplam = 0
        for satis in self.Satislar:
            toplam += int(satis.get_tutar())
        return toplam

    def __str__(self):
        return f"Ad: {self.get_satici_adi()}\t Toplam Satis: {str(self.satislariTopla())}"

class Satis():
    def __init__(self, tutar = 0, cins = "Bilinmiyor"):
        self.__tutar = tutar
        self.__cins = cins

    def get_tutar(self):
        return self.__tutar

    def get_cins(self):
        return self.__cins

    def __str__(self):
        return f"Satilan Urun: {self.get_cins()}\t Fiyati: {self.get_tutar()}"

def main():
    magazalar = []

    kontrol = True

    while kontrol:
        secim = input("\nYapmak istediginiz islemi seciniz\n"
                      "1) Magaza Ekle\n"
                      "2) Magaza Islemleri\n"
                      "0) Programi Sonlandir\n")

        if secim == '1':
            magazaAdi = input("Magaza adini giriniz: ")
            magazaEklemeKontrol = True
            for magaza in magazalar:
                if magaza.get_magaza_adi() == magazaAdi:
                    print("Bu isimde bir magaza zaten var!\n")
                    magazaEklemeKontrol = False
                    break

            if magazaEklemeKontrol:
                eklenecekMagaza = Magaza(magazaAdi)
                magazalar.append(eklenecekMagaza)
                print("Magaza basariyla eklendi...\n")

        elif secim == '2':
            if len(magazalar) == 0:
                print("Sistemde hic magaza bulunmamaktadir, lutfen once magaza ekleyiniz!\n")

            else:
                magazaAdi = input("Islem yapmak istediginiz magazanin adini giriniz: ")

                secilenMagaza = None
                for magaza in magazalar:
                    if magaza.get_magaza_adi() == magazaAdi:
                        secilenMagaza = magaza
                        break
                if secilenMagaza is None:
                    print("Bu isimde bir magaza bulunamadi!\n")

                else:
                    magazadaKal = True
                    while magazadaKal:
                        magazaIslem = input("\nYapmak istediginiz islemi seciniz\n"
                                      "1) Calisan Ekle\n"
                                      "2) Satis Yap\n"
                                     
                                      "0) Programi Sonlandir\n")

                        if magazaIslem == '1':
                            calisanAdi = input("Calisan adini giriniz: ")

                            calisanEklemeKontrol = True
                            for calisan in secilenMagaza.Calisanlar:
                                if calisan.get_satici_adi() == calisanAdi:
                                    print("Bu magazada bu isime sahip bir calisan zaten var!\n")
                                    calisanEklemeKontrol = False
                                    break

                            if calisanEklemeKontrol:
                                eklenecekCalisan = Calisan(calisanAdi, [])
                                secilenMagaza.calisanEkle(eklenecekCalisan)
                                print("Calisan basariyla eklendi...\n")

                        elif magazaIslem == '2':
                            if len(secilenMagaza.Calisanlar) == 0:
                                print("Magazada hic calisan bulunmamakta, lutfen once calisan ekleyiniz!\n")

                            else:
                                secilecekCalisanAdi = input("Satis yapmak istediginiz calisanin adini giriniz: ")

                                secilenCalisan = None
                                for calisan in secilenMagaza.Calisanlar:
                                    if calisan.get_satici_adi() == secilecekCalisanAdi:
                                        secilenCalisan = calisan
                                        break
                                if secilenCalisan is None:
                                    print("Bu isimde bir calisan bulunamadi!\n")

                                else:
                                    tutar = int(input("Satis fiyatini giriniz: "))
                                    cins = input("Urun cinsini giriniz: ")

                                    yapilanSatis = Satis(tutar, cins)
                                    secilenCalisan.satisEkle(yapilanSatis)
                                    print("Satis basarili...\n")

                        elif magazaIslem == '3':
                            if len(secilenMagaza.Calisanlar) == 0:
                                print("Magazada hic calisan bulunmamakta, lutfen once calisan ekleyiniz!\n")

                            else:
                                secilecekCalisanAdi = input("Satislarini gormek istediginiz calisanin adini giriniz: ")

                                secilenCalisan = None
                                for calisan in secilenMagaza.Calisanlar:
                                    if calisan.get_satici_adi() == secilecekCalisanAdi:
                                        secilenCalisan = calisan
                                        break
                                if secilenCalisan is None:
                                    print("Bu isimde bir calisan bulunamadi!\n")

                                else:
                                    secilenCalisan.satislariListele()

                        elif magazaIslem == '4':
                            secilenMagaza.magazaBilgileri()

                        elif magazaIslem == '5':
                            print("Ana menuye yonlendiriliyorsunuz...\n")
                            magazadaKal = False
                        elif magazaIslem == '0':
                            print("Program Sonlandiriliyor...")
                            kontrol = False
                            break
                        else:
                            print("Gecersiz bir islem girdiniz!\n")

        elif secim == '0':
            print("Program Sonlandiriliyor...")
            break

        else:
            print("Gecersiz bir islem girdiniz!\n")

main()