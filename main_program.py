import argparse
from cryptography.fernet import Fernet

# Ladda nyckeln från fil
def load_key(key_fil):
    try:
        with open(key_fil, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Nyckelfilen {key_fil} hittades inte.")
        exit(1)

# Kryptera fil
def encrypt_file(key, in_fil, nya_fil):
    fernet = Fernet(key)
    
    # Läs innehållet från in-filen
    try:
        with open(in_fil, 'rb') as file:
            fil_data = file.read()
        
        # Kryptera innehållet
        encrypted_data = fernet.encrypt(fil_data)

        # Spara den krypterade datan till en output-fil
        with open(nya_fil, 'wb') as file:
            file.write(encrypted_data)
        
        print(f"Filen {in_fil} har krypterats och sparats som {nya_fil}.")
    except FileNotFoundError:
        print(f"Input-filen {in_fil} hittades inte.")
        exit(1)

# Dekryptera fil
def decrypt_file(key, in_fil, nya_fil):
    fernet = Fernet(key)
    
    # Läs innehållet från den krypterade filen
    try:
        with open(in_fil, 'rb') as file:
            encrypted_data = file.read()

        # Dekryptera innehållet
        decrypted_data = fernet.decrypt(encrypted_data)

        # Spara den dekrypterade datan till en output-fil
        with open(nya_fil, 'wb') as file:
            file.write(decrypted_data)

        print(f"Filen {in_fil} har dekrypterats och sparats som {nya_fil}.")
    except FileNotFoundError:
        print(f"Input-filen {in_fil} hittades inte.")
        exit(1)
    except ImportError:
        print("Dekrypteringen misslyckades. Fel nyckel eller korrupt fil.")
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vill du kryptera eller dekryptera en fil?")
    
    # Lägg till kommandoradsargument
    parser.add_argument("operation", choices=["kryptera", "dekryptera"], help="Välj operation: kryptera eller dekryptera.")
    parser.add_argument("key_fil", help="Filen som innehåller krypteringsnyckeln.")
    parser.add_argument("in_fil", help="Ange filen som ska krypteras eller dekrypteras.")
    parser.add_argument("nya_fil", help="Ange filnamnet för att spara den krypterade eller dekrypterade filen.")

    args = parser.parse_args()
    
    # Ladda nyckeln
    key = load_key(args.key_fil)
    
    # Utför kryptering eller dekryptering
    if args.operation == "kryptera":
        encrypt_file(key, args.in_fil, args.nya_fil)
    elif args.operation == "dekryptera":
        decrypt_file(key, args.in_fil, args.nya_fil)