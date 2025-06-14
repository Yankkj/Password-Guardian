import hashlib
import requests

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    headers = {
        "User-Agent": "PasswordGuardian-App"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        hashes = response.text.splitlines()
        found_breaches = []

        for h in hashes:
            hash_suffix, count = h.split(':')
            if hash_suffix == suffix:
                found_breaches.append({"hash_suffix": hash_suffix, "count": int(count)})

        return found_breaches

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar ao Have I Been Pwned?: {e}")
        return None

def get_breach_details_placeholder():
    return "Para mais detalhes sobre os vazamentos, visite https://haveibeenpwned.com"

if __name__ == "__main__":
    test_passwords = ["password", "123456", "senha123", "MinhaSenhaMuitoSegura!@#123"]
    for p in test_passwords:
        print(f"Verificando senha: '{p}'")
        breaches = check_password_breach(p)
        if breaches is not None:
            if breaches:
                print(f"  Vazamentos encontrados para '{p}':")
                for b in breaches:
                    print(f"    - Exposta {b['count']} vezes em vazamentos conhecidos.")
                print("  " + get_breach_details_placeholder())
            else:
                print(f"  Nenhum vazamento encontrado para '{p}'.")
        print("-" * 30)