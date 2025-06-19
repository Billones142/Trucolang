import sys
import re

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
    """
    Análisis léxico robusto: reconoce comandos válidos (de una o dos palabras, con o sin repetición),
    sin depender de los espacios. Lanza error si encuentra un token inválido.
    """
    # Lista de comandos válidos, ordenados por longitud descendente para evitar ambigüedad
    commands = sorted(VALID_COMMANDS, key=lambda x: -len(x))
    # Construir patrón regex para todos los comandos, permitiendo (n) al final
    pattern = r"|".join([re.escape(cmd) + r"(\(\d+\))?" for cmd in commands])
    token_regex = re.compile(pattern)
    tokens: list[str] = []
    pos = 0
    while pos < len(source_code):
        match = token_regex.match(source_code, pos)
        if match:
            token_str = match.group(0)
            # Verificar si es repetición
            rep_match = re.match(r"^(.*)\((\d+)\)$", token_str)
            if rep_match:
                cmd = rep_match.group(1)
                count = int(rep_match.group(2))
                tokens.extend([cmd] * count)
            else:
                tokens.append(token_str)
            pos = match.end()
        elif source_code[pos].isspace():
            pos += 1  # Ignorar espacios
        else:
            # Encontró un token inválido
            end = pos + 20 if pos + 20 < len(source_code) else len(source_code)
            raise SyntaxError(f"Token no reconocido cerca de: '{source_code[pos:end]}'")
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
    print("Iniciando compilación...\n")
    tokens = lexer(source_code)
    print("Tokens:", tokens)

    syntax_analyzer(tokens)
    print("Análisis sintáctico correcto")

    brainfuck_code = generate_brainfuck(tokens)

    return brainfuck_code

# Ejemplo de uso:
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <archivo_entrada> [archivo_salida]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.bf"
    
    with open(input_file, 'r') as file:
        code = file.read()
    try:
        bf_code = compile_trucolang(code)
        with open(output_file, "w") as outputFile:
            outputFile.write(bf_code)
        print(f"Código Brainfuck generado exitosamente en: {output_file}")
    except (LexicalError, SyntaxError) as e:
        print("Error durante la compilación:", e)
