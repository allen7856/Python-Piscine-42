def ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", "r")
        print("Connection established...")
        print("\nRECOVERED DATA:")
        print(f.read())
        print("Data recovery complete. Storage unit disconnected.")
        f.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    ancient_text()
