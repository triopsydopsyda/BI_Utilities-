# FastQ Filtrator
**FastQ Filtrator** is a toolkit for working with the FastQ format. The program filters reads based on the following factors.


Authors:
* **Software:** *Anastasia Shipuniva*, Saint-Petersburg, Russia.
* **Idea:** *Nikita Vaulin*,
Bioinformatic Institution.


## FastQ Filtrator
FastQ Filtrator — is a utility for working with sequences in FastQ format. The program filters reads based on the following criteria:
- Sequence length (length bounds)
- GC content (gc bounds)
- Average quality (quality threshold)

The program is designed for pre-processing sequencing data before performing bioinformatics analysis.

## Installation

For *Linux* and *Mac OS*, *Windows* and *other OS*: download `fastq_filtrator,py`, `filtered_modules.py`, `dna_rna_modules.py`, run the command `filter_fastq()`

## Input

For running the program you have to provide parametrs:
    :param seqs: dict, name: sequence; quality
    :param gc_bounds: max and min boundary values of the GC composition.
                    default = (0,100)
    :param length_bounds: max and min boundary for the length of the seq
                    default = (0, 2*32)
    :param quality_threshold: threshold for the quality (phred33).
                    default = 0

## Output 

The program will return you filtered dictionary. 