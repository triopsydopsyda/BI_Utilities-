from dna_rna_modules import (transcription,
                             reversion,
                             complementation,
                             reverse_compl,
                             primers
                             )
from filtered_modules import gc_count
from filtered_modules import quality_count

NUCLEOTIDES: list = ["A", "a", "T", "t", "G", "g", "C", "c", "U", "u"]
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
        if not set(seq).issubset(NUCLEOTIDES):
            return "Something went wrong. Check your input."
    if function in fn_map:
        ret = fn_map[function](*sequence)
        if len(ret) == 1:
            return ret[0]
        return ret
    else:
        return "Something went wrong. Check your input."


def filter_fastq(
        seqs: dict[str, tuple[str, str]],
        gc_bounds: tuple[float, float] = (0, 100),
        length_bounds: tuple[int, int] = (0, 2**32),
        quality_threshold: float = 0
) -> dict[str, tuple[str, str]]:

    """
    Filters your fastq data.

    :param seqs: dict, name: sequence; quality
    :param gc_bounds: max and min boundary values of the GC composition.
                    default = (0,100)
    :param length_bounds: max and min boundary for the length of the seq
                    default = (0, 2*32)
    :param quality_threshold: threshold for the quality (phred33).
                    default = 0
    :return:
    filtered dict.
    """

    if isinstance(gc_bounds, (int, float)):
        gc_bounds = [0, gc_bounds]

    if isinstance(length_bounds, (int, float)):
        length_bounds = [0, length_bounds]

    filtered_seqs = {}
    for name, (sequence, quality) in seqs.items():
        seq_length = len(sequence)
        if not (length_bounds[0] <= seq_length <= length_bounds[1]):
            continue
        gc_content = gc_count(sequence)
        if not (gc_bounds[0] <= gc_content <= gc_bounds[1]):
            continue
        average_quality = quality_count(quality)
        if average_quality < quality_threshold:
            continue
        filtered_seqs[name] = (sequence, quality)

    return filtered_seqs
