# DNA-project
The goal of the system is to load, analyze, manipulate and save DNA sequences.

DNA sequences are composed of four types of nucleotides;
The nucleotides are marked A , G , C and T.
A full DNA molecule usually consists of two strands, connected to each other in
base-pair connections: As with Ts, and Cs with Gs.
Three successive nucleotides generate a codon, which might be chemically "read" in
various ways.
The system will interact with the user through a CLI (Command Line Interface) that
uses the standard I/O. Using that interface, the user will be able to load DNA
sequences from files, to analyze them, to manipulate them (e.g., by extracting
sequence slices or by modifying the sequence), and to store modified sequences and
reports.

### commands implemented 
1. new command
2. load command
3. dup command
4. slice command
5. replace command
6. del command
7. list command
8. save command
9. find command
10. findall command
11. len command
12. count command
13. quit command 
14. batch commands:
  create, run, list, show, save, load

### design patterns
1.singelton - for each command andforthe db

2.factory

3.command

4.abstract classes
  
