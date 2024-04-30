from ttkbootstrap import Style
from tkinter import ttk
import webbrowser

style = Style(theme='minty')  # superhero, journal, minty, lumen, morph, darkly

window = style.master
window.geometry("450x250")
window.resizable(0, 0)
window.title("Birim Dönüştürücü")

# create a notebook
notebook = ttk.Notebook(window)
notebook.pack(padx= 10, pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=420, height=260)
frame2 = ttk.Frame(notebook, width=420, height=260)
frame3 = ttk.Frame(notebook, width=420, height=260)
frame4 = ttk.Frame(notebook, width=420, height=260)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(frame1, text='Uzunluk')
notebook.add(frame2, text='Alan')
notebook.add(frame3, text='Hacim')
notebook.add(frame4, text='Hakkında')

tip_uzunluk = ("km","m","cm","mm")
tip_agirlik = ("ton","kg","gr","mg")
tip_hacim = ("hl","dal","l","dl","ml")
tip_zaman = ("saat","dakika","saniye")

# UZUNLUK SEKMESİ WİDGET'LARI
etiket_girdi_deger_uzn = ttk.Label(frame1, text = "Değer :")
etiket_girdi_deger_uzn.place(x=20, y=20)

entry_girdi_uzn = ttk.Entry(frame1, width=22)
entry_girdi_uzn.insert(0,"0")
entry_girdi_uzn.place(x=120,y=20)

etiket_girdi_birim_uzn = ttk.Label(frame1, text = "Girdi Birimi :")
etiket_girdi_birim_uzn.place(x=20, y=60)

kombo_uzunluk_girdi_uzn = ttk.Combobox(frame1, state='readonly')
kombo_uzunluk_girdi_uzn["values"] = tip_uzunluk
kombo_uzunluk_girdi_uzn.place(x=120,y=60)

etiket_cikti_birim_uzn = ttk.Label(frame1, text = "Çıktı Birimi :")
etiket_cikti_birim_uzn.place(x=20, y=100)

kombo_uzunluk_cikti_uzn = ttk.Combobox(frame1, state='readonly')
kombo_uzunluk_cikti_uzn["values"] = tip_uzunluk
kombo_uzunluk_cikti_uzn.place(x=120,y=100)

etiket_sonuc_uzn = ttk.Label(frame1, text = "Sonuç :")
etiket_sonuc_uzn.place(x=20, y=140)

entry_sonuc_uzn = ttk.Entry(frame1, width=22, state="disabled")
entry_sonuc_uzn.insert(0,"0")
entry_sonuc_uzn.place(x=120,y=140)

buton_donustur_uzn = ttk.Button(frame1, text = "Dönüştür")
buton_donustur_uzn.place(x=320,y=140)

# HAKKINDA
etiket_uygulama = ttk.Label(frame4, text = "\nBirim Dönüştürücü\nVersiyon 0.2")
etiket_uygulama.pack(expand="YES")

def baglantiya_git(url):
    webbrowser.open_new(url)

etiket_baglanti = ttk.Button(frame4, text = "https://github.com/mhalil/birim-donusturme", style='Link.TButton')
etiket_baglanti.pack(expand="YES")
etiket_baglanti.bind("<Button-1>", lambda e: baglantiya_git("https://github.com/mhalil/birim-donusturme"))

window.mainloop()