import os

output_directory = os.path.join(os.path.dirname(os.getcwd()), "filtered")


def save_filtered(
    output_data: dict[str, tuple[str, str]], output_directory: str
) -> None:
    """
    Save filtered FASTQ data to a specified directory, creating a new file if it already exists.
    :param output_data: dict, name: sequence; quality
    :param output_directory:  An output director.
    :return: None, but saved your file to a "filtered" directory.
    """
    base_filename = "output_fastq"

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = os.path.join(output_directory, f"{base_filename}.fastq")

    if os.path.exists(output_file):
        counter = 1
        while True:
            new_filename = f"{base_filename}_{counter}.fastq"
            new_output_file = os.path.join(output_directory, new_filename)
            if not os.path.exists(new_output_file):
                output_file = new_output_file
                break
            counter += 1
    with open(output_file, "w") as file:
        for index, (sequence, quality) in output_data.items():
            file.write(f"{sequence}\n")
