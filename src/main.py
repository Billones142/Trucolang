import sys

TRUCOLANG_TO_BRAINFUCK = {
    "quiero": "+",           # Incrementar memoria
    "no quiero": "-",        # Decrementar memoria
    "envido": ">",           # Mover puntero a la derecha
    "falta envido": "<",     # Mover puntero a la izquierda
    "truco": "[",            # Inicio de bucle
    "vale cuatro": "]",      # Fin de bucle
    "venite": ".",           # Imprimir caracter
    "quedate": ","           # Leer caracter
}

VALID_COMMANDS = set(TRUCOLANG_TO_BRAINFUCK.keys())

class LexicalError(Exception):
    pass

class SyntaxError(Exception):
    pass

def lexer(source_code: str) -> list[str]:
    """Análisis léxico: convierte texto en tokens válidos"""
    words = source_code.split()
    tokens: list[str] = []
    i = 0
    while i < len(words):
        if i + 1 < len(words) and f"{words[i]} {words[i+1]}" in VALID_COMMANDS:
            tokens.append(f"{words[i]} {words[i+1]}")
            i += 2
        elif words[i] in VALID_COMMANDS:
            tokens.append(words[i])
            i += 1
        else:
            raise SyntaxError(f"Token no reconocido '{words[i]}'.")
            i += 1
    return tokens

def syntax_analyzer(tokens: list[str]) -> bool:
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

def generate_brainfuck(tokens: list[str]) -> str:
    """Traducción: convierte tokens a código Brainfuck"""
    return ''.join(TRUCOLANG_TO_BRAINFUCK[token] for token in tokens)

def compile_trucolang(source_code: str) -> str:
    print("📘 Iniciando compilación...\n")
    tokens = lexer(source_code)
    print("✅ Tokens:", tokens)

    syntax_analyzer(tokens)
    print("✅ Análisis sintáctico correcto")

    brainfuck_code = generate_brainfuck(tokens)

    return brainfuck_code

# Ejemplo de uso:
if __name__ == "__main__":
    with open(sys.argv[1], 'r') as file:
        code = file.read()
    try:
        bf_code = compile_trucolang(code)
        with open("output.brainfuck", "w") as outputFile:
            outputFile.write(bf_code)
    except (LexicalError, SyntaxError) as e:
        print("❌ Error durante la compilación:", e)
