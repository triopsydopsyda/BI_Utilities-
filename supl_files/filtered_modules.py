def gc_count(sequence: str) -> float:
    cn = sequence.count("C")
    gn = sequence.count("G")
    gc_value = (cn + gn) / len(sequence) * 100
    return gc_value


def quality_count(quality: str) -> float:
    quality_value = sum(ord(char) - 33 for char in quality) / len(quality)
    return quality_value


def filter_fastq(
    seqs: dict[str, tuple[str, str]],
    gc_bounds: tuple[float, float] = (0, 100),
    length_bounds: tuple[int, int] = (0, 2**32),
    quality_threshold: float = 0,
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

    if not filtered_seqs:
        return f"There are no suitable sequences"

    return filtered_seqs
