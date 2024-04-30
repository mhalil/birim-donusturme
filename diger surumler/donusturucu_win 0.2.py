from ttkbootstrap import Style
from tkinter import ttk

style = Style(theme='superhero')  # superhero, journal, minty, lumen, morph, darkly

window = style.master
window.geometry("400x250")
window.resizable(0, 0)
window.title("Birim Dönüştürücü")

# create a notebook
notebook = ttk.Notebook(window)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=250)
frame2 = ttk.Frame(notebook, width=400, height=250)
frame3 = ttk.Frame(notebook, width=400, height=250)
frame4 = ttk.Frame(notebook, width=400, height=250)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)
frame4.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='Uzunluk')
notebook.add(frame2, text='Alan')
notebook.add(frame3, text='Hacim')
notebook.add(frame4, text='Hakkında')

# tipler = [["ağırlık","ton","kg","gr","mg"],["uzunluk","km","m","cm","mm"],["hacim","hl","dal","l","dl","ml"],["zaman","saat","dakika","saniye"]]
tipler_uzunluk = ("km","m","cm","mm")
tip = ""
tip_indis = 0

birim1_etiket = ttk.Label(frame1, text = "Değer :")
birim1_etiket.place( x=20, y=20)

birim1 = ttk.Entry(frame1, width=22)
birim1.insert(0,"0")
birim1.place(x=120,y=20)

birim1_tip_etiket = ttk.Label(frame1, text = "Girdi Birimi :")
birim1_tip_etiket.place(x=20, y=60)

birim1_tip = ttk.Combobox(frame1, state='readonly')
birim1_tip["values"] = tipler_uzunluk
birim1_tip.place(x=120,y=60)

birim2_tip_etiket = ttk.Label(frame1, text = "Çıktı Birimi :")
birim2_tip_etiket.place(x=20, y=100)

birim2_tip = ttk.Combobox(frame1, state='readonly')
birim2_tip["values"] = tipler_uzunluk
birim2_tip.place(x=120,y=100)

birim_sonuc_etiket = ttk.Label(frame1, text = "Sonuç :")
birim_sonuc_etiket.place( x=20, y=140)

birim_sonuc = ttk.Entry(frame1, width=22, state="disabled")
birim_sonuc.insert(0,"0")
birim_sonuc.place(x=120,y=140)

donustur_btn = ttk.Button(frame1, text = "Dönüştür")
donustur_btn.place(x=300,y=140)

window.mainloop()