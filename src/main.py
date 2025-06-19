TRUCOLANG_TO_BRAINFUCK = {
    "retruco": "+",
    "envido": "-",
    "quiero": ">",
    "no quiero": "<",
    "truco": "[",
    "vale cuatro": "]",
    "flor": ".",
    "muestra": ","
}

VALID_COMMANDS = set(TRUCOLANG_TO_BRAINFUCK.keys())

class LexicalError(Exception):
    pass

class SyntaxError(Exception):
    pass

def lexer(source_code):
    """Análisis léxico: convierte texto en tokens válidos"""
    words = source_code.split()
    tokens = []
    i = 0
    while i < len(words):
        if i + 1 < len(words) and f"{words[i]} {words[i+1]}" in VALID_COMMANDS:
            tokens.append(f"{words[i]} {words[i+1]}")
            i += 2
        elif words[i] in VALID_COMMANDS:
            tokens.append(words[i])
            i += 1
        else:
            # Ignorar comentarios o texto inválido, o lanzar error si se desea
            print(f"Advertencia: token no reconocido '{words[i]}'. Se ignora.")
            i += 1
    return tokens

def syntax_analyzer(tokens):
    """Análisis sintáctico: verifica que los bucles estén balanceados"""
    balance = 0
    for token in tokens:
        if token == "truco":
            balance += 1
        elif token == "vale cuatro":
            balance -= 1
        if balance < 0:
            raise SyntaxError("Error: 'vale cuatro' sin un 'truco' previo.")
    if balance != 0:
        raise SyntaxError("Error: cantidad desigual de 'truco' y 'vale cuatro'.")
    return True

def generate_brainfuck(tokens):
    """Traducción: convierte tokens a código Brainfuck"""
    return ''.join(TRUCOLANG_TO_BRAINFUCK[token] for token in tokens)

def compile_trucolang(source_code):
    print("📘 Iniciando compilación...\n")
    tokens = lexer(source_code)
    print("✅ Tokens:", tokens)

    syntax_analyzer(tokens)
    print("✅ Análisis sintáctico correcto")

    brainfuck_code = generate_brainfuck(tokens)
    print("✅ Código Brainfuck generado:\n", brainfuck_code)

    return brainfuck_code

# Ejemplo de uso:
if __name__ == "__main__":
    code = """
    retruco retruco retruco quiero truco retruco no quiero vale cuatro flor
    """
    try:
        bf_code = compile_trucolang(code)
    except (LexicalError, SyntaxError) as e:
        print("❌ Error durante la compilación:", e)
