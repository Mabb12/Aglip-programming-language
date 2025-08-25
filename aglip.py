def compile_aglip(code):
    py_code = f"counter = 0\nmemory = [0] * 256\n"
    in_loop = 0
    counter = 0
    for cmd in code:
        if cmd == "A": py_code += "    " * in_loop + "memory[counter] = (memory[counter] + 1) % 257\n" # Add
        elif cmd == "G": # Go
            py_code += "    " * in_loop + "counter = (counter + 1) % 257\n"
            counter += 1 % 257
        elif cmd == "L": # Loop
            if in_loop == 0:
                py_code += "    " * in_loop + f"while memory[{counter}] != memory[{counter + 1}]:\n"
            in_loop = 1 - in_loop
        elif cmd == "I": py_code += "    " * in_loop + "memory[counter] = int(input()) % 257\n" # Input
        elif cmd == "P": py_code += "    " * in_loop + "print(memory[counter])\n" # Print
    return py_code

if __name__ == "__main__":
    program = 'AGLIP'
    python_code = compile_aglip(program)
    print(python_code)
    exec(python_code)