from numpy import uint16

with open("input", "r") as inputText:
    instructions = inputText.readlines()


def operation_handling(target: str, source: str, override: uint16 | None) -> None:

    if "AND" in source:
        operands = source.split(" AND ")

        try: circuit[target] = uint16(operands[0]) & circuit[operands[1]]
        except ValueError: circuit[target] = circuit[operands[0]] & circuit[operands[1]]

    elif "OR" in source:
        operands = source.split(" OR ")
        circuit[target] = circuit[operands[0]] | circuit[operands[1]]

    elif "NOT" in source:
        circuit[target] = ~ circuit[source.split(" ")[1]]

    elif "LSHIFT" in source:
        operands = source.split(" LSHIFT ")

        try: circuit[target] = circuit[operands[0]] << uint16(operands[1])
        except ValueError: circuit[target] = circuit[operands[0]] << circuit[operands[1]]

    elif "RSHIFT" in source:
        operands = source.split(" RSHIFT ")
        try: circuit[target] = circuit[operands[0]] >> uint16(operands[1])
        except ValueError: circuit[target] = circuit[operands[0]] >> circuit[operands[1]]

    else:
        try:
            if target == "b" and override is not None: circuit['b'] = override
            else: circuit[target] = uint16(source)
        except ValueError: circuit[target] = uint16(circuit[source])

circuit: dict = {}
def emulate_circuit(override: uint16 | None = None) -> int:
    while 'a' not in circuit:

        for instruction in instructions:

            connections: list[str] = instruction.split(" -> ")
            target: str = connections[1].rstrip()
            source: str = connections[0]
            del(connections)

            if target not in circuit:

                try: operation_handling(target, source, override)
                except KeyError: continue

    return circuit['a']

b_value = emulate_circuit()
print(b_value)

circuit = {}
print(emulate_circuit(b_value))