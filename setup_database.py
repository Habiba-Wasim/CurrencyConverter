# import sqlite3

# def setup_database():
#     conn = sqlite3.connect("currency.db")
#     cursor = conn.cursor()
    
#     # Create table
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS exchange_rates (
#             currency TEXT PRIMARY KEY,
#             rate REAL
#         )
#     ''')

#     # Insert sample data (Ek martaba chalana hai)
#     sample_rates = [
#         ("USD", 82.5),
#         ("EUR", 90.2),
#         ("GBP", 103.7),
#         ("PKR", 277.8),
#         ("AUD", 55.6)
#     ]

#     cursor.executemany("INSERT OR REPLACE INTO exchange_rates VALUES (?, ?)", sample_rates)
#     conn.commit()
#     conn.close()
#     print("✅ Currency Database Ready!")

# if __name__ == "__main__":
#     setup_database()






















import sqlite3

def setup_database():
    conn = sqlite3.connect("currency.db")
    cursor = conn.cursor()
    
    # Create table (agar exist nahi karti toh create hogi)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS exchange_rates (
            currency TEXT PRIMARY KEY,
            rate REAL
        )
    ''')

    # New Currency List (Aap jitni marzi currencies add kar sakte hain)
    updated_rates = [
        ("USD", 82.5),
        ("EUR", 90.2),
        ("GBP", 103.7),
        ("PKR", 277.8),
        ("AUD", 55.6),
        ("CAD", 60.3),
        ("JPY", 0.55),
        ("CNY", 11.8),
        ("AED", 22.5),
        ("SAR", 21.9),
        ("TRY", 5.3)
    ]

    cursor.executemany("INSERT OR REPLACE INTO exchange_rates VALUES (?, ?)", updated_rates)
    conn.commit()
    conn.close()
    print("✅ Currency Database Updated with More Currencies!")

if __name__ == "__main__":
    setup_database()
