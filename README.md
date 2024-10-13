# Bioinformatics Utilities
Utilities contains **FastQ Filtrator** and **BIO Files processor**

Authors:
* **Software:** *Anastasia Shipunova*, Saint-Petersburg, Russia.
* **Idea:** *Nikita Vaulin*,
Bioinformatic Institution.

**FastQ Filtrator** is a toolkit for working with the FastQ format. The program filters reads based on the following factors.

## FastQ Filtrator
FastQ Filtrator — is a utility for working with sequences in FastQ format. The program filters reads based on the following criteria:
- Sequence length (length bounds)
- GC content (gc bounds) 
- Average quality (quality threshold)

The program is designed for pre-processing sequencing data before performing bioinformatics analysis. As intput you should provide FASTQ file, and program will save filtered sequences 

## Installation

For *Linux* and *Mac OS*, *Windows* and *other OS*: download `fastq_filtrator,py`, `filtered_modules.py`, `dna_rna_modules.py`, `save_modules.py` from [repository](https://github.com/triopsydopsyda/BI_Utilities-/tree/HW4_2) 

#### Example:
```python filter_fastq('file_name.fastq', 'function')```


### Input:

For running the program you have to provide parameters:
> param file_name: The name of the input FASTQ file.
> 
> param gc_bounds: max and min boundary values of the GC composition, default = (0,100)
> 
> param length_bounds: max and min boundary for the length of the seq, default = (0, 2*32)
> 
> param quality_threshold: threshold for the quality (phred33), default = 0
> 
> :return:
    output_fastq_№.fastq file with filtered sequences saved to a "filtered" directory

## Output 

The program will save filtered sequences as a file to a new folder "filtered"

## BIO Files processor
Contains two main features:
- to convert a multi-lined fastq file to a single-lined; 
- to parse blast output and collect names of proteins sequences producing significant alignments.

### Function 1: `convert_multiline_fasta_to_oneline`

This function converts a multi-line FASTA file into a single-line format.

#### Parameters:
- `input_fasta` (str): The name of the input multi-line FASTA file (e.g., `"input.fasta"`).
- `output_fasta` (str, optional): The name of the output single-line FASTA file. Defaults to `"bio_files_result"`.

#### Example:
```python convert_multiline_fasta_to_oneline("input.fasta", "output.fasta")```

### Function 2: `parse_blast_output`

This function parses a BLAST output file to extract sequences that show significant alignments. It focuses on capturing the first column of data from the relevant section of the BLAST output.

#### Parameters:
- `input_fasta` (str): The name of the input BLAST output file (e.g., `"example_blast_results.txt"`).
- `output_fasta` (str): The name of the output file where the parsed sequences will be saved (e.g., `"parsed_blast_results.txt"`).

#### Returns:
- None: The function saves the extracted sequences to the specified output file in the current directory.

#### Example:
```python parse_blast_output("example_blast_results.txt", "parsed_blast_results.txt") ```

