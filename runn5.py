import cv2
import json
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import Label, Entry, Button, Listbox, Scrollbar, END, messagebox, Frame

# Toplam fiyat değişkeni
total_price = 0

def load_product_data():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_product_data(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)

def fill_product_fields(barcode):
    products = load_product_data()
    if barcode in products:
        entry_barcode.delete(0, END)
        entry_name.delete(0, END)
        entry_price.delete(0, END)
        entry_barcode.insert(0, barcode)
        entry_name.insert(0, products[barcode]['name'])
        entry_price.insert(0, products[barcode]['price'])

def add_product():
    global total_price, scanned_barcodes
    barcode = entry_barcode.get()
    name = entry_name.get()
    price = entry_price.get()
    
    if not barcode or not name or not price:
        messagebox.showwarning("Uyarı", "Tüm alanları doldurun!")
        return
    
    products = load_product_data()
    products[barcode] = {"name": name, "price": price}
    save_product_data(products)
    update_product_list()
    
    # Manuel ekleme yapıldığı için toplam fiyat sıfırlanıp yeniden hesaplanmalı
    total_price = 0
    scanned_barcodes.clear()
    
    messagebox.showinfo("Başarılı", "Ürün eklendi!")


def update_product_list():
    global total_price
    total_price = 0
    products = load_product_data()
    listbox.delete(0, END)
    for barcode, details in products.items():
        listbox.insert(END, f"{barcode} - {details['name']} - {details['price']} TL")

def delete_product():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Uyarı", "Silmek için bir ürün seçin!")
        return
    
    index = selected[0]
    product_key = listbox.get(index).split(" - ")[0]
    products = load_product_data()
    
    if product_key in products:
        del products[product_key]
        save_product_data(products)
        update_product_list()
        messagebox.showinfo("Başarılı", "Ürün silindi!")
scanned_barcodes = set()
def show_product_info(barcode_data):
    global total_price
    print(f"Barkod Algılandı: {barcode_data}")
    
    # Barkodu giriş kutusuna yazdır
    entry_barcode.delete(0, END)
    entry_barcode.insert(0, barcode_data)
    
    products = load_product_data()
    product = products.get(barcode_data)

    if product:
        entry_name.delete(0, END)
        entry_price.delete(0, END)
        entry_name.insert(0, product['name'])
        entry_price.insert(0, product['price'])
        
        # Eğer barkod daha önce okutulmamışsa toplam fiyata ekle
        if barcode_data not in scanned_barcodes:
            total_price += float(product['price'])
            scanned_barcodes.add(barcode_data)  # Barkodu kaydet
        
        label_info.config(text=f"Ürün: {product['name']}\nFiyat: {product['price']} TL")
    else:
        entry_name.delete(0, END)
        entry_price.delete(0, END)
        label_info.config(text=f"Bilinmeyen Barkod: {barcode_data}")

    label_total_price.config(text=f"Toplam Fiyat: {total_price:.2f} TL")
    tk_window.update_idletasks()

# Kamera başlat
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FPS, 60)
cap.set(cv2.CAP_PROP_FOCUS, 90)

# Tkinter Arayüzü
tk_window = tk.Tk()
tk_window.title("Barkod Okuyucu ve Ürün Yönetimi")
tk_window.geometry("800x650")
tk_window.configure(bg="#f0f0f0")

frame_top = Frame(tk_window, bg="#d9d9d9", padx=20, pady=20)
frame_top.pack(fill="x")

label_info = Label(frame_top, text="Barkod Okutunuz", font=("Arial", 16, "bold"), fg="#333", bg="#d9d9d9")
label_info.pack(pady=5)

label_total_price = Label(frame_top, text="Toplam Fiyat: 0.00 TL", font=("Arial", 14, "bold"), fg="#333", bg="#d9d9d9")
label_total_price.pack(pady=5)

frame_inputs = Frame(tk_window, bg="#f0f0f0")
frame_inputs.pack(pady=10)

label_barcode = Label(frame_inputs, text="Barkod:", bg="#f0f0f0")
label_barcode.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_barcode = Entry(frame_inputs, width=40)
entry_barcode.grid(row=0, column=1, padx=10, pady=5)

label_name = Label(frame_inputs, text="Ürün Adı:", bg="#f0f0f0")
label_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_name = Entry(frame_inputs, width=40)
entry_name.grid(row=1, column=1, padx=10, pady=5)

label_price = Label(frame_inputs, text="Fiyat:", bg="#f0f0f0")
label_price.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_price = Entry(frame_inputs, width=40)
entry_price.grid(row=2, column=1, padx=10, pady=5)

frame_buttons = Frame(tk_window, bg="#f0f0f0")
frame_buttons.pack(pady=10)

btn_add = Button(frame_buttons, text="Ürün Ekle", command=add_product, bg="#4CAF50", fg="white", padx=20)
btn_add.pack(side="left", padx=5)

btn_delete = Button(frame_buttons, text="Ürün Sil", command=delete_product, bg="#f44336", fg="white", padx=20)
btn_delete.pack(side="left", padx=5)

frame_list = Frame(tk_window, bg="#f0f0f0")
frame_list.pack(pady=10, fill="both", expand=True)

listbox = Listbox(frame_list, width=80, height=10, font=("Arial", 12))
listbox.pack(side="left", padx=10, pady=10, fill="both", expand=True)

scrollbar = Scrollbar(frame_list)
scrollbar.pack(side="right", fill="y")

update_product_list()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    for barcode in decode(frame):
        barcode_data = barcode.data.decode('utf-8')
        print(f"Barkod: {barcode_data}")
        show_product_info(barcode_data)

    cv2.imshow('Barkod Tarayıcı', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    tk_window.update()

cap.release()
cv2.destroyAllWindows()
