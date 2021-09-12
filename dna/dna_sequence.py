import re


class Dna_Sequence:
    def __init__(self, dna_string, dna_name, dna_id):
        if not self.__valid_dna(dna_string):
            raise ValueError

        self.__dna = dna_string
        self.__dna_name = dna_name
        self.__dna_id = dna_id

    def get_dna(self):
        return self.__dna

    def get_dna_name(self):
        return self.__dna_name

    def get_dna_id(self):
        return self.__dna_id

    def set_dna(self, dna):
        try:
            self.__valid_dna(dna)
        except ValueError:
            return "DNA string not valid"
        self.__dna = dna

    def insert(self, nucleotide, index):
        """insert nucleotide to DNA string[index]"""
        if nucleotide not in ['A', 'C', 'T', 'G', 'a', 'c', 't', 'g']:
            raise ValueError
        try:
            temp = list(self.__dna)
            temp[index] = nucleotide
            self.__dna = "".join(temp)
        except IndexError as e:
            return f"error {e}"

    def find_sub_string_index(self, sub):
        """
        find start index in dna seq of substring sub
        :param sub: substring to find index
        """
        try:
            return self.__dna.index(sub)
        except ValueError:
            raise ValueError

    def find_all_sub(self, sub):
        """
        find all indexes of sub string in dna seq
        :param sub:sub string to find
        :return:array of indexes
        """
        try:
            return [i for i in range(len(self.__dna)) if self.__dna.startswith(sub, i)]
        except ValueError:
            raise ValueError

    def assignment(self, other):
        if isinstance(other, str):
            if not self.__valid_dna(other):
                return "invalid assignment value"
            self.__dna = other
        elif isinstance(other, Dna_Sequence):
            self.__dna = other.get_dna()
        else:
            return "invalid value"

    def __str__(self):
        return f"[{self.__dna_id}] {self.__dna_name}: {self.__dna}"

    def __eq__(self, other):
        if isinstance(other, str):
            return self.__dna == other
        else:
            return self.__dna == other.get_dna()

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, item):
        try:
            return self.__dna[item]
        except IndexError:
            print(IndexError)

    def __setitem__(self, key, value):
        if value not in ['A', 'C', 'T', 'G', 'a', 'c', 't', 'g']:
            raise ValueError
        try:
            temp = list(self.__dna)
            temp[key] = value
            self.__dna = "".join(temp)
        except IndexError:
            print(IndexError)

    def __len__(self):
        return len(self.__dna)

    # privet method to check DNA string validation
    def __valid_dna(self, dna):
        for char in dna:
            if char not in ['A', 'C', 'T', 'G', 'a', 'c', 't', 'g']:
                return False
        return True
