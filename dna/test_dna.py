from dna.dna_sequence import Dna_Sequence


def test_DNA():
    dna_1 = Dna_Sequence("AAGGCC")
    dna_2 = Dna_Sequence("ACGT")
    assert dna_1 == "AAGGCC"
    dna_1.assignment("ACGT")
    assert dna_1 == dna_2
    assert dna_1 != "AAA"
    assert len(dna_1) == 4
    dna_1.insert('C', 0)
    assert dna_1[0] == 'C'
    print(dna_1, dna_2)
