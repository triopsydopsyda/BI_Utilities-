REPLACE_VALUES: dict[str, str] = {"t": "u", "T": "U"}
COMPLEMENT_VALUES: dict[str, str] = {
    "A": "T",
    "a": "t",
    "G": "C",
    "g": "c",
    "U": "A",
    "u": "a",
    "T": "A",
    "t": "a",
    "C": "G",
    "c": "g",
}
nucleotides: list[str] = ["A", "a", "T", "t", "G", "g", "C", "c", "U", "u"]


def transcription(*sequence: list[str], replace_values=REPLACE_VALUES) -> list:
    result = []
    for seq in sequence:
        for previous, new in replace_values.items():
            seq = seq.replace(previous, new)
        result.append(seq)
    return result


def complementation(*sequence: list[str], complement_values=COMPLEMENT_VALUES) -> list:
    result = []
    translation_table = str.maketrans(complement_values)
    for seq in sequence:
        seq = seq.translate(translation_table)
        result.append(seq)
    return result


def reversion(*sequence: list[str]) -> list:
    result = []
    for seq in sequence:
        seq = seq[::-1]
        result.append(seq)
    return result


def reverse_compl(*sequence: list[str]) -> list:
    rev_seq = reversion(*sequence)
    result = []
    for seq in rev_seq:
        rev_compl = complementation(seq)
        result.extend(rev_compl)
    return result


def primers(*sequence: list[str]) -> list:
    result = []
    for seq in sequence:
        seq = seq.upper()
        An = seq.count("A")
        Tn = seq.count("T")
        Cn = seq.count("C")
        Gn = seq.count("G")
        Temp = 2 * (An + Tn) + 4 * (Cn + Gn)
        length = len(seq)
        ans = f"Annealing temp. is {Temp}°C, length is {length}n"
        result.append(ans)
    return result


fn_map: dict[str, callable] = {
    "transcribe": transcription,
    "reverse": reversion,
    "complement": complementation,
    "reverse_complement": reverse_compl,
    "get_primers_info": primers,
}


def run_dna_rna_tools(*args: str) -> str:
    """
    Manipulate with the DNA or RNA sequence.

    :param:
    - sequence(str): sequence to work with
    - function(str):
       "transcribe" to make transcribed sequence;
        "reverse" to reverse the sequence;
        "complement" to make complement sequence;
        "reverse_complement" to make reverse-complement sequence;
        "get_primers_info" function provides the annealing temp.
        and the length of your sequence.
    :return:
    - str/list, the result of the function
    """
    *sequence, function = args

    for seq in sequence:
        if not set(seq).issubset(nucleotides):
            return "Something went wrong. Check your input."
    if function in fn_map:
        ret = fn_map[function](*sequence)
        if len(ret) == 1:
            return ret[0]
        return ret
    else:
        return "Something went wrong. Check your input."
