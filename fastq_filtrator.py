from dna_rna_modules import (
    transcription,
    reversion,
    complementation,
    reverse_compl,
    primers,
)

import os
from save_modules import save_filtered
from filtered_modules import filter_fastq


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


def read_and_filter_save_fastq(
    file_name: str,
    gc_bounds: tuple[float, float] = (0, 100),
    length_bounds: tuple[int, int] = (0, 2**32),
    quality_threshold: float = 0,
):
    """
    Function that reads input fastq file, filters it and save suitable sequences to the new directory as a file.
    :param file_name: The name of the input FASTQ file.
    :param gc_bounds: max and min boundary values of the GC composition.
                    default = (0,100)
    :param length_bounds: max and min boundary for the length of the seq
                    default = (0, 2*32)
    :param quality_threshold: threshold for the quality (phred33).
                    default = 0
    :return:
    output_fastq_№.fastq file with filtered sequences saved to a "filtered" directory
    """
    data_dir = os.getcwd()
    output_directory = os.path.join(data_dir, "filtered")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(os.path.join(data_dir, file_name), "r") as fastq_file:
        fastq_data = {}
        while True:
            index = fastq_file.readline().strip()
            if not index:
                break
            sequence = fastq_file.readline().strip()
            fastq_file.readline().strip()
            quality = fastq_file.readline().strip()
            fastq_data[index] = (sequence, quality)
    filtered_data = filter_fastq(
        fastq_data, gc_bounds, length_bounds, quality_threshold
    )
    return save_filtered(filtered_data, output_directory)


filtered_data = read_and_filter_fastq("example_fastq.fastq", gc_bounds=(5, 2**20))
