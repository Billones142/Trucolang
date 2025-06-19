# Trucolang

Trucolang es un compilador que traduce código escrito en un lenguaje inspirado en el Truco argentino a Brainfuck.

## ¿Cómo usar el compilador?

1. **Clona este repositorio y navega a la carpeta:**
   ```bash
   git clone https://github.com/Billones142/Trucolang
   cd Trucolang
   ```

2. **Prepara tu entorno:**
   - Asegúrate de tener Python 3 instalado.

3. **Escribe tu programa en Trucolang:**
   - Crea un archivo de texto, por ejemplo `holaMundo.truco`, con instrucciones válidas de Trucolang.

4. **Compila tu archivo:**
   Ejecuta el compilador desde la terminal:
   ```bash
   python src/main.py holaMundo.truco
   ```
   Esto generará un archivo `output.brainfuck` con el código Brainfuck resultante.

## Ejemplo de uso

Supón que tienes el siguiente archivo `holaMundo.truco`:
```
retruco retruco retruco retruco retruco retruco retruco retruco retruco retruco retruco retruco retruco quiero retruco retruco retruco retruco retruco retruco retruco retruco retruco retruco quiero retruco retruco retruco retruco retruco retruco retruco retruco retruco retruco quiero flor
```

Compílalo con:
```
python src/main.py holaMundo.truco
```

El resultado estará en `output.brainfuck`.

## Comandos de Trucolang

| Brainfuck | Significado                        | Trucolang       |
|-----------|------------------------------------|-----------------|
| +         | Incrementar memoria                | quiero          |
| -         | Decrementar memoria                | no quiero       |
| >         | Mover puntero a la derecha         | envido          |
| <         | Mover puntero a la izquierda       | falta envido    |
| [         | Inicio de bucle                    | truco           |
| ]         | Fin de bucle                       | vale cuatro     |
| .         | Imprimir caracter                  | venite          |
| ,         | Leer caracter                      | quedate         |

- Los comentarios o palabras no reconocidas serán ignorados.
- El compilador verifica que los bucles (`truco` y `vale cuatro`) estén balanceados.

## Licencia

Este proyecto está bajo la licencia MIT.
