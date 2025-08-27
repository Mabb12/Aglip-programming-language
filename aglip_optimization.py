def compile_aglip(code):
    py_code = "counter = 0\nmemory = [0] * 256\n"
    in_loop = 0
    i = 0
    len_code = len(code)

    while i < len_code:
        cmd = code[i]

        if cmd == "A":  # Add
            count = 1
            while i + count < len_code and code[i + count] == "A":
                count += 1
            py_code += "    " * in_loop + f"memory[counter] = (memory[counter] + {count}) % 256\n"
            i += count

        elif cmd == "G":  # Go 
            count = 1
            while i + count < len_code and code[i + count] == "G":
                count += 1
            py_code += "    " * in_loop + f"counter = (counter + {count}) % 256\n"
            i += count

        elif cmd == "L":  # Loop 
            if in_loop == 0:
                py_code += "    " * in_loop + "while memory[counter] != 0:\n"
                in_loop += 1
            else:
                in_loop -= 1
            i += 1

        elif cmd == "I":  # Input
            py_code += "    " * in_loop + "memory[counter] = int(input('Input: ')) % 256\n"
            i += 1

        elif cmd == "P":  # Print
            py_code += "    " * in_loop + "print(f'Output: {memory[counter]}')\n"
            i += 1

        else: 
            i += 1

    return py_code


def run_aglip(code):
    """Безопасное выполнение AGLIP кода"""
    try:
        python_code = compile_aglip(code)
        print("Скомпилированный Python код:")
        print("=" * 40)
        print(python_code)
        print("=" * 40)
        print("Результат выполнения:")
        exec(python_code)
    except Exception as e:
        print(f"Ошибка выполнения: {e}")


if __name__ == "__main__":
    program3 = 'AAA'

    run_aglip(program3)

