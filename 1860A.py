def find_valid_bracket_sequence(s):
    n = len(s)
    valid_sequences = generate_valid_sequences(2 * n)
    
    for sequence in valid_sequences:
        if s not in sequence:
            return sequence
    
    return "Impossible"

def generate_valid_sequences(length):
    sequences = []
    generate_sequences("", length, 0, 0, sequences)
    return sequences

def generate_sequences(sequence, length, open_count, close_count, sequences):
    if len(sequence) == length:
        sequences.append(sequence)
        return
    
    if open_count < length // 2:
        generate_sequences(sequence + "(", length, open_count + 1, close_count, sequences)
    
    if close_count < open_count:
        generate_sequences(sequence + ")", length, open_count, close_count + 1, sequences)

num = int(input())

for _ in range(num):
    parseq = input()
    print(find_valid_bracket_sequence(parseq))
