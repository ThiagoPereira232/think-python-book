def right_justify(s):
    ns = s
    while len(ns) < 70:
        ns += s
    return ns

print(right_justify('monty'))
