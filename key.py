from cryptography.fernet import Fernet

def generate_key(fil_namn):
    # Generera en ny symmetrisk nyckel
    key = Fernet.generate_key()
    
    # Spara nyckeln till en fil
    with open(fil_namn, 'wb') as key_file:
        key_file.write(key)
    
    print(f"Nyckel genererad och sparad i {fil_namn}")

if __name__ == "__main__":
    # Du kan ange filnamnet här, t.ex. 'secret.key'
    fil_namn = "secret.key"
    generate_key(fil_namn)