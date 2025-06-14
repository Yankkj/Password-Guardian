import re

def analyze_password_strength(password):
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*()_+={}\[\]:;"\'<>,.?/\\|`~-]', password))

    strength_score = 0
    feedback = []

    if length >= 12:
        strength_score += 2
        feedback.append("Comprimento adequado (12+ caracteres).")
    elif length >= 8:
        strength_score += 1
        feedback.append("Comprimento razoável (8-11 caracteres).")
    else:
        feedback.append("Senha muito curta (menos de 8 caracteres).")

    if has_upper:
        strength_score += 1
        feedback.append("Contém letras maiúsculas.")
    else:
        feedback.append("Adicione letras maiúsculas para maior segurança.")

    if has_lower:
        strength_score += 1
        feedback.append("Contém letras minúsculas.")
    else:
        feedback.append("Adicione letras minúsculas para maior segurança.")

    if has_digit:
        strength_score += 1
        feedback.append("Contém números.")
    else:
        feedback.append("Adicione números para maior segurança.")

    if has_special:
        strength_score += 2
        feedback.append("Contém caracteres especiais.")
    else:
        feedback.append("Adicione caracteres especiais para maior segurança.")

    # Pontos de dedução para padrões comuns
    if re.search(r'(.)\1{2,}', password): # 3 ou mais caracteres repetidos
        strength_score -= 1
        feedback.append("Evite caracteres repetidos sequencialmente.")
    if re.search(r'123|abc|password|qwerty', password, re.IGNORECASE): # Padrões simples
        strength_score -= 2
        feedback.append("Evite padrões comuns ou palavras-chave.")

    if strength_score >= 7:
        strength = "Muito Forte"
    elif strength_score >= 5:
        strength = "Forte"
    elif strength_score >= 3:
        strength = "Boa"
    elif strength_score >= 1:
        strength = "Fraca"
    else:
        strength = "Muito Fraca"

    return {"strength": strength, "score": strength_score, "feedback": feedback}

if __name__ == "__main__":
    test_passwords = ["senha123", "Senha@12345", "123456", "MinhaSenhaMuitoSegura!@#123", "aaaaaaaa"]
    for p in test_passwords:
        result = analyze_password_strength(p)
        print(f"Senha: '{p}'")
        print(f"Força: {result['strength']} (Score: {result['score']})")
        for f in result['feedback']:
            print(f"- {f}")
        print("-" * 30)