from ttkbootstrap import Style
from tkinter import ttk

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

etiket_girdi_deger = ttk.Label(frame1, text = "Değer :")
etiket_girdi_deger.place(x=20, y=20)

entry_girdi = ttk.Entry(frame1, width=22)
entry_girdi.insert(0,"0")
entry_girdi.place(x=120,y=20)

etiket_girdi_birim = ttk.Label(frame1, text = "Girdi Birimi :")
etiket_girdi_birim.place(x=20, y=60)

kombo_uzunluk_girdi = ttk.Combobox(frame1, state='readonly')
kombo_uzunluk_girdi["values"] = tip_uzunluk
kombo_uzunluk_girdi.place(x=120,y=60)

etiket_cikti_birim = ttk.Label(frame1, text = "Çıktı Birimi :")
etiket_cikti_birim.place(x=20, y=100)

kombo_uzunluk_cikti = ttk.Combobox(frame1, state='readonly')
kombo_uzunluk_cikti["values"] = tip_uzunluk
kombo_uzunluk_cikti.place(x=120,y=100)

etiket_sonuc = ttk.Label(frame1, text = "Sonuç :")
etiket_sonuc.place(x=20, y=140)

entry_sonuc = ttk.Entry(frame1, width=22, state="disabled")
entry_sonuc.insert(0,"0")
entry_sonuc.place(x=120,y=140)

buton_donustur = ttk.Button(frame1, text = "Dönüştür")
buton_donustur.place(x=320,y=140)

window.mainloop()