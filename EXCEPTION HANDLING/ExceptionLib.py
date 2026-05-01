def save_book(title, price):
    try:
        # Using 'a' for append mode
        with open("library_db.txt", "a") as f:
            f.write(f"{title}, {price}\n")
    except PermissionError:
        print("Error: The database file is currently locked by another program.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("--- Welcome to the Bulletproof Library ---")
    
    while True:
        try:
            title = input("\nEnter book title (or 'exit'): ").strip()
            if title.lower() == 'exit':
                break
            
            if not title:
                raise ValueError("Book title cannot be empty!")

            # This is where a ValueError is most likely to happen
            price = float(input(f"Enter price for '{title}': "))
            
            save_book(title, price)
            print("Book saved successfully!")

        except ValueError as ve:
            print(f"Invalid Input: {ve}. Please enter a valid number for the price.")
        except KeyboardInterrupt:
            print("\nProgram paused. Please use 'exit' to quit safely.")
        finally:
            print("System check: Ready for next entry.")

if __name__ == "__main__":
    main()  
