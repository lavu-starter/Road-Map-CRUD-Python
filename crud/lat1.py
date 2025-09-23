import sqlite3

# --- Inisialisasi Database ---
def init_db():
    conn = sqlite3.connect("ecommerce.db")
    cur = conn.cursor()
    # Membuat tabel produk jika belum ada
    cur.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        stock INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("Tabel 'products' siap digunakan!")

# --- Fungsi CRUD ---
# Fungsi tambah produk
def tambah_produk(nama, harga, stok):
    conn = sqlite3.connect("ecommerce.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
        (nama, harga, stok)
    )
    conn.commit()
    conn.close()
    print(f"Produk '{nama}' berhasil ditambahkan!")

# Fungsi tampilkan produk
def tampilkan_produk():
    conn = sqlite3.connect("ecommerce.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    conn.close()

    if rows:
        print("\nDaftar Produk dari Database:")
        for row in rows:
            print(f"ID: {row[0]}, Nama: {row[1]}, Harga: Rp{row[2]}, Stok: {row[3]}")
    else:
        print("Belum ada produk.")

# --- Main Program ---
if __name__ == "__main__":
    init_db()

    # Simulasi tambah produk
    tambah_produk("Laptop", 7000000, 10)
    tambah_produk("Smartphone", 3500000, 20)

    # Tampilkan produk
    tampilkan_produk()
