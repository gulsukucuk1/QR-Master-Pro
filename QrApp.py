import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
import cv2
from pyzbar.pyzbar import decode
import webbrowser
import os
import numpy as np 

class ProfesyonelQrSistemi:
    def __init__(self, ana_pencere):
        self.ana_pencere = ana_pencere
        self.ana_pencere.title("QR Master Pro - Karakter Hatasi Cozuldu")
        self.ana_pencere.geometry("450x550")
        self.ana_pencere.configure(bg="#ffffff")

        self.baslik = tk.Label(ana_pencere, text="QR MASTER", font=("Arial", 24, "bold"), bg="#ffffff", fg="#1e272e")
        self.baslik.pack(pady=20)

        tk.Label(ana_pencere, text="Link veya Metin Yaziniz:", bg="#ffffff", font=("Arial", 10)).pack()
        self.giris = tk.Entry(ana_pencere, width=35, font=("Arial", 12), bd=2, relief="groove")
        self.giris.pack(pady=10, ipady=5)

        self.btn_olustur = tk.Button(ana_pencere, text="QR KODU OLUSTUR VE KAYDET", command=self.qr_uret, 
                                     bg="#10ac84", fg="white", font=("Arial", 11, "bold"), width=30, height=2, cursor="hand2")
        self.btn_olustur.pack(pady=10)

        self.btn_kamera = tk.Button(ana_pencere, text="KAMERADAN TARA VE AC", command=self.kameradan_oku, 
                                    bg="#2e86de", fg="white", font=("Arial", 11, "bold"), width=30, height=2, cursor="hand2")
        self.btn_kamera.pack(pady=10)

        self.btn_dosya = tk.Button(ana_pencere, text="DOSYADAN TARA VE AC", command=self.dosyadan_oku, 
                                   bg="#f39c12", fg="white", font=("Arial", 11, "bold"), width=30, height=2, cursor="hand2")
        self.btn_dosya.pack(pady=10)

    def baglantiyi_ac(self, veri):
        if veri.startswith("http") or veri.startswith("www"):
            link = veri if veri.startswith("http") else "http://" + veri
            webbrowser.open(link)
            messagebox.showinfo("Baglanti Aciliyor", "Su adrese gidiliyor:\n" + link)
        else:
            messagebox.showinfo("QR Icerigi", "Okunan Metin:\n" + veri)

    def qr_uret(self):
        metin = self.giris.get()
        if not metin:
            messagebox.showwarning("Uyari", "Lutfen bir icerik girin!")
            return
        
        yol = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
        if yol:
            img = qrcode.make(metin)
            img.save(yol)
            messagebox.showinfo("Tamam", "QR Kod basariyla kaydedildi.")

    def kameradan_oku(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret: break
            
            detaylar = decode(frame)
            for d in detaylar:
                icerik = d.data.decode('utf-8')
                cap.release()
                cv2.destroyAllWindows()
                self.baglantiyi_ac(icerik)
                return
            
            cv2.imshow("QR Kodunu Kameraya Gosterin (Cikis: Q)", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        cap.release()
        cv2.destroyAllWindows()

    def dosyadan_oku(self):
        yol = filedialog.askopenfilename(filetypes=[("Resimler", "*.png *.jpg *.jpeg")])
        if yol:
            try:
                with open(yol, "rb") as f:
                    chunk = f.read()
                nparr = np.frombuffer(chunk, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                if img is not None:
                    detaylar = decode(img)
                    if detaylar:
                        icerik = detaylar[0].data.decode('utf-8')
                        self.baglantiyi_ac(icerik)
                    else:
                        messagebox.showerror("Hata", "Bu resimde bir QR kod bulunamadi!")
                else:
                    messagebox.showerror("Hata", "Resim dosyasi acilamadi!")
            except Exception as e:
                messagebox.showerror("Sistem Hatasi", "Dosya okuma hatasi: " + str(e))

if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = ProfesyonelQrSistemi(pencere)
    pencere.mainloop()