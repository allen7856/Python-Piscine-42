def crisis_handler(filename: str, routine: bool) -> None:
    label: str = "ROUTINE ACCESS" if routine else "CRISIS ALERT"
    print(f"{label}: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(f"RESPONSE: Unexpected anomaly detected - {e}")
        print("STATUS: Crisis contained, damage assessed")


def crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt", False)
    crisis_handler("classified_vault.txt", False)
    crisis_handler("standard_archive.txt", True)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    crisis_response()
