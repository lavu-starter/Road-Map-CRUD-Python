import sqlite3

# ----------------- Database Setup -----------------
def init_db():
    conn = sqlite3.connect("cart.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            price INTEGER NOT NULL,
            quantity INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ----------------- CRUD Functions -----------------
def add_item(item, price, quantity):
    conn = sqlite3.connect("cart.db")
    c = conn.cursor()
    c.execute("INSERT INTO cart (item, price, quantity) VALUES (?, ?, ?)", (item, price, quantity))
    conn.commit()
    conn.close()
    print(f"{quantity} {item} ditambahkan ke keranjang.")

def view_cart():
    conn = sqlite3.connect("cart.db")
    c = conn.cursor()
    c.execute("SELECT * FROM cart")
    rows = c.fetchall()
    conn.close()

    if not rows:
        print("\nKeranjang kosong.\n")
    else:
        print("\nIsi Keranjang:")
        total = 0
        for row in rows:
            id_, item, price, qty = row
            subtotal = price * qty
            total += subtotal
            print(f"{id_}. {item} ({qty} x {price}) = {subtotal}")
        print(f"Total Belanja: Rp {total}\n")

def update_item(item_id, new_price=None, new_quantity=None):
    conn = sqlite3.connect("cart.db")
    c = conn.cursor()
    if new_price is not None:
        c.execute("UPDATE cart SET price=? WHERE id=?", (new_price, item_id))
    if new_quantity is not None:
        c.execute("UPDATE cart SET quantity=? WHERE id=?", (new_quantity, item_id))
    conn.commit()
    conn.close()
    print(f"Barang dengan ID {item_id} berhasil diperbarui.")

def remove_item(item_id):
    conn = sqlite3.connect("cart.db")
    c = conn.cursor()
    c.execute("DELETE FROM cart WHERE id=?", (item_id,))
    conn.commit()
    conn.close()
    print(f"Barang dengan ID {item_id} dihapus dari keranjang.")

def checkout():
    conn = sqlite3.connect("cart.db")
    c = conn.cursor()
    c.execute("SELECT * FROM cart")
    rows = c.fetchall()

    if not rows:
        print("Keranjang kosong, tidak bisa checkout.")
    else:
        print("\n=== Checkout ===")
        total = 0
        for row in rows:
            id_, item, price, qty = row
            subtotal = price * qty
            total += subtotal
            print(f"- {item} ({qty} x {price}) = {subtotal}")
        print(f"Total Belanja: Rp {total}")
        print("Terima kasih sudah berbelanja!\n")
        # kosongkan keranjang
        c.execute("DELETE FROM cart")
        conn.commit()

    conn.close()

# ----------------- Program Menu CLI -----------------
def main():
    init_db()
    while True:
        print("""
======= MENU KERANJANG (SQLite) =======
1. Tambah Barang
2. Lihat Keranjang
3. Update Barang
4. Hapus Barang
5. Checkout
6. Keluar
""")
        choice = input("Pilih menu (1-6): ")

        if choice == "1":  # CREATE
            item = input("Nama barang: ")
            price = int(input("Harga barang: "))
            quantity = int(input("Jumlah: "))
            add_item(item, price, quantity)

        elif choice == "2":  # READ
            view_cart()

        elif choice == "3":  # UPDATE
            view_cart()
            item_id = int(input("Masukkan ID barang yang mau diupdate: "))
            print("Kosongkan jika tidak ingin diubah")
            new_price = input("Harga baru: ")
            new_quantity = input("Jumlah baru: ")
            update_item(
                item_id,
                new_price=int(new_price) if new_price else None,
                new_quantity=int(new_quantity) if new_quantity else None
            )

        elif choice == "4":  # DELETE
            view_cart()
            item_id = int(input("Masukkan ID barang yang mau dihapus: "))
            remove_item(item_id)

        elif choice == "5":  # CHECKOUT
            checkout()

        elif choice == "6":  # EXIT
            print("Keluar dari program. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid, coba lagi!")

if __name__ == "__main__":
    main()
