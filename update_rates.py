import sqlite3

def update_rates():
    conn = sqlite3.connect("currency.db")
    cursor = conn.cursor()

    # Yahan apni updated currency rates dalen
    updated_rates = [
        ("USD", 83.0),
        ("EUR", 91.5),
        ("GBP", 104.8),
        ("PKR", 278.2),
        ("AUD", 56.3)
    ]

    cursor.executemany("INSERT OR REPLACE INTO exchange_rates VALUES (?, ?)", updated_rates)
    conn.commit()
    conn.close()
    print("✅ Exchange Rates Updated!")

if __name__ == "__main__":
    update_rates()
