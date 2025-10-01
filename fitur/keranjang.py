class ShoppingCart:
    def __init__(self):
        self.cart = {}

    # CREATE
    def add_item(self, item, price, quantity=1):
        if item in self.cart:
            self.cart[item]["quantity"] += quantity
        else:
            self.cart[item] = {"price": price, "quantity": quantity}
        print(f"{quantity} {item} ditambahkan ke keranjang.")

    # READ
    def view_cart(self):
        if not self.cart:
            print("\nKeranjang kosong.\n")
        else:
            print("\nIsi Keranjang:")
            total = 0
            for item, details in self.cart.items():
                subtotal = details["price"] * details["quantity"]
                total += subtotal
                print(f"- {item} ({details['quantity']} x {details['price']}) = {subtotal}")
            print(f"Total Belanja: Rp {total}\n")

    # UPDATE
    def update_item(self, item, new_price=None, new_quantity=None):
        if item in self.cart:
            if new_price is not None:
                self.cart[item]["price"] = new_price
            if new_quantity is not None:
                self.cart[item]["quantity"] = new_quantity
            print(f"{item} berhasil diperbarui.")
        else:
            print(f"{item} tidak ada di keranjang.")

    # DELETE
    def remove_item(self, item):
        if item in self.cart:
            del self.cart[item]
            print(f"{item} dihapus dari keranjang.")
        else:
            print(f"{item} tidak ada di keranjang.")

    # CHECKOUT
    def checkout(self):
        if not self.cart:
            print("Keranjang kosong, tidak bisa checkout.")
        else:
            print("\n=== Checkout ===")
            self.view_cart()
            print("Terima kasih sudah berbelanja!")
            self.cart.clear()


# ---------------- Program Menu CLI ----------------
def main():
    cart = ShoppingCart()
    while True:
        print("""
======= MENU KERANJANG =======
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
            cart.add_item(item, price, quantity)

        elif choice == "2":  # READ
            cart.view_cart()

        elif choice == "3":  # UPDATE
            item = input("Nama barang yang mau diupdate: ")
            print("Kosongkan jika tidak ingin diubah")
            new_price = input("Harga baru: ")
            new_quantity = input("Jumlah baru: ")
            cart.update_item(
                item,
                new_price=int(new_price) if new_price else None,
                new_quantity=int(new_quantity) if new_quantity else None
            )

        elif choice == "4":  # DELETE
            item = input("Nama barang yang mau dihapus: ")
            cart.remove_item(item)

        elif choice == "5":  # CHECKOUT
            cart.checkout()

        elif choice == "6":  # EXIT
            print("Keluar dari program. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid, coba lagi!")


if __name__ == "__main__":
    main()
