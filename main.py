import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("fitness_tracker.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS fitness (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    activity TEXT NOT NULL,
    duration INTEGER NOT NULL,
    calories_burned INTEGER NOT NULL
)
''')
conn.commit()

# Function to add a fitness record
def add_entry(date, activity, duration, calories_burned):
    cursor.execute("INSERT INTO fitness (date, activity, duration, calories_burned) VALUES (?, ?, ?, ?)",
                   (date, activity, duration, calories_burned))
    conn.commit()
    print("✅ Entry added successfully!")

# Function to view all records
def view_entries():
    cursor.execute("SELECT * FROM fitness")
    records = cursor.fetchall()
    
    if not records:
        print("⚠️ No records found!")
        return
    
    print("\n📊 Fitness Records:")
    print("=" * 50)
    for row in records:
        print(f"ID: {row[0]}, Date: {row[1]}, Activity: {row[2]}, Duration: {row[3]} mins, Calories Burned: {row[4]}")
    print("=" * 50)

# Function to update a record
def update_entry(entry_id, new_date, new_activity, new_duration, new_calories):
    cursor.execute("UPDATE fitness SET date = ?, activity = ?, duration = ?, calories_burned = ? WHERE id = ?",
                   (new_date, new_activity, new_duration, new_calories, entry_id))
    conn.commit()
    print("✅ Entry updated successfully!")

# Function to delete a record
def delete_entry(entry_id):
    cursor.execute("DELETE FROM fitness WHERE id = ?", (entry_id,))
    conn.commit()
    print("🗑️ Entry deleted successfully!")

# Main menu
def main():
    while True:
        print("\n🏋️ FITNESS TRACKER MENU 🏋️")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Update Entry")
        print("4. Delete Entry")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            activity = input("Enter activity name: ")
            duration = int(input("Enter duration (minutes): "))
            calories = int(input("Enter calories burned: "))
            add_entry(date, activity, duration, calories)

        elif choice == "2":
            view_entries()

        elif choice == "3":
            entry_id = int(input("Enter ID of the entry to update: "))
            new_date = input("Enter new date (YYYY-MM-DD): ")
            new_activity = input("Enter new activity name: ")
            new_duration = int(input("Enter new duration (minutes): "))
            new_calories = int(input("Enter new calories burned: "))
            update_entry(entry_id, new_date, new_activity, new_duration, new_calories)

        elif choice == "4":
            entry_id = int(input("Enter ID of the entry to delete: "))
            delete_entry(entry_id)

        elif choice == "5":
            print("👋 Exiting... Stay fit! 💪")
            break

        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

# Close the database connection when the script ends
conn.close()
