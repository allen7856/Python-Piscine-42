def archive_creation() -> None:
    filename: str = "new_discovery.txt"
    entries: list[str] = [
            "[ENTRY 001] New quantum algorithm discovered",
            "[ENTRY 002] Efficiency increased by 347%",
            "[ENTRY 003] Archived by Data Archivist trainee",
            ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")

    f = open(filename, "w")

    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    for entry in entries:
        f.write(entry + "\n")
        print(f"{entry}")

    f.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    archive_creation()
