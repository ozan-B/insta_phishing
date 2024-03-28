import subprocess
import os
import shutil


def klasor_kopyala(kaynak_dizin, hedef_dizin):#insta_login_clone dizininin içindekileri  /var/www/html/ dizinine kaydeder .
    try:
        # Hedef dizini oluştur
        if not os.path.exists(hedef_dizin):
            os.makedirs(hedef_dizin)
        
        # Kaynak dizin içindeki tüm dosyaları kopyala
        for dosya in os.listdir(kaynak_dizin):
            dosya_yolu = os.path.join(kaynak_dizin, dosya)
            hedef_dosya_yolu = os.path.join(hedef_dizin, dosya)
            if os.path.isfile(dosya_yolu):
                shutil.copy(dosya_yolu, hedef_dosya_yolu)
            elif os.path.isdir(dosya_yolu):
                shutil.copytree(dosya_yolu, hedef_dosya_yolu)
        
        print("Dosyalar başarıyla kopyalandı.")
    
    except Exception as e:
        print("Bir hata oluştu:", str(e))

def apache_start():#apache server başlatır
    try:
        # subprocess.run ile komutu çalıştırırken sudo için sudo komutu ve giriş parametrelerini kullanıyoruz.
        subprocess.run(['sudo', 'service', 'apache2', 'start'], check=True)
        print("Apache başlatıldı.")
    except subprocess.CalledProcessError as e:
        print("Hata oluştu:", e)


# Kullanım örneği
kaynak_dizin = "./insta_login_clone/"
hedef_dizin = "/var/www/html/"
klasor_kopyala(kaynak_dizin, hedef_dizin)

# Fonksiyonu çağırarak Apache'yi başlatma
apache_start()