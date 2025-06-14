import secrets
import string

def generate_secure_password(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation 

    if not characters:
        raise ValueError("Nenhum tipo de caractere selecionado para gerar a senha.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_passphrase(num_words=4, separator='-'):
    words = [
        "abelha", "barco", "cadeira", "dado", "elefante", "foguete", "girassol",
        "hidroaviao", "igreja", "jacare", "kiwi", "leao", "macaco", "nuvem",
        "oculos", "piano", "queijo", "raio", "sapato", "tigre", "uva", "violao",
        "xadrez", "zebra", "arvore", "bicicleta", "chocolate", "diamante",
        "eletricidade", "farinha", "guitarra", "helicoptero", "internet",
        "janela", "ketchup", "lampada", "montanha", "navio", "orquidea",
        "paralelepipedo", "quadro", "radio", "sorvete", "telescopio", "universo",
        "ventilador", "whisky", "xilofone", "yoga", "ziper",
        "andar", "brincar", "cantar", "desenhar", "escrever", "voar", "gostar",
        "habitar", "imaginar", "jogar", "ler", "montar", "nadar", "observar",
        "pular", "querer", "rir", "saltar", "tocar", "usar", "viajar",
        "alegre", "brilhante", "colorido", "divertido", "elegante", "fofo",
        "grande", "harmonioso", "incrivel", "jovial", "leve", "magnifico",
        "novo", "original", "paciente", "quente", "radiante", "suave",
        "tranquilo", "unico", "valioso", "wild", "extraordinario", "zeloso",
        "aurora", "borboleta", "cachoeira", "deserto", "estrela", "floresta",
        "geada", "horizonte", "inverno", "jardim", "lago", "mar", "neve",
        "outono", "primavera", "quintal", "rocha", "sol", "trovoada", "universo",
        "vulcao", "wave", "xisto", "yosemite", "zephyr",
        "algoritmo", "browser", "codigo", "dados", "email", "firewall",
        "github", "hardware", "internet", "javascript", "keyboard", "linux",
        "monitor", "network", "output", "python", "query", "robot", "software",
        "terminal", "usb", "virtual", "website", "xml", "youtube", "zip"
    ]
    
    if num_words > len(words):
        raise ValueError("Número de palavras excede o disponível na lista.")

    selected_words = secrets.SystemRandom().sample(words, num_words)
    return separator.join(selected_words).capitalize() # Capitaliza a primeira letra

if __name__ == "__main__":
    print("Gerando senhas seguras:")
    print(f"Senha de 12 caracteres: {generate_secure_password(12)}")
    print(f"Senha de 20 caracteres (apenas letras e números): {generate_secure_password(20, use_special=False)}")
    print(f"Frase-senha de 3 palavras: {generate_passphrase(3)}")
    print(f"Frase-senha de 5 palavras: {generate_passphrase(5, '_')}")