import os


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: str = "bio_files_result"
) -> None:
    """
    Convert a multi-line FASTA file into a single-line FASTA format.

    :param input_fasta: The name of the input multi-line FASTA file.
    :param output_fasta: The name of the output single-line FASTA file (default is 'bio_files_result').
    :return: None, but new single-lined FASTA file will bw saved in your current directory.
    """

    data_dir = os.getcwd()
    output_path = os.path.join(data_dir, output_fasta)

    with (
        open(os.path.join(data_dir, input_fasta)) as bio_file,
        open(output_path, "w") as out_file,
    ):
        sequence = []
        for line in bio_file:
            line = line.strip()
            if line.startswith(">"):
                if sequence:
                    out_file.write("".join(sequence) + "\n")
                out_file.write(line + "\n")
                sequence = []
            else:
                sequence.append(line)
        if sequence:
            out_file.write("".join(sequence) + "\n")


def parse_blast_output(input_fasta: str, output_fasta: str) -> None:
    """
    Parse the BLAST output and extract the first column of sequences producing significant alignments.
    :param input_fasta: The name of the input BLAST output file.
    :param output_fasta: The name of the output file to save the parsed sequences.
    :return: None, but new file will bw saved in your current directory.
    """
    data_dir = os.getcwd()
    output_path = os.path.join(data_dir, output_fasta)

    with (
        open(os.path.join(data_dir, input_fasta)) as blast_file,
        open(output_path, "w") as out_blast,
    ):
        capture_sequences = False
        for line in blast_file:
            line = line.strip()
            if line.startswith("Sequences producing significant alignments:"):
                blast_file.readline().strip()
                blast_file.readline().strip()
                capture_sequences = True
            elif capture_sequences:
                if line:
                    first_column = line.replace("    ", "\t", 1).split("\t")[0]
                    out_blast.write(first_column + "\n")
                    capture_sequences = False


parse_blast_output("example_blast_results.txt", "parsed_blast_results.txt")
