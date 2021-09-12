from data.dna_data import DNA_Data


class Command:
    """
    interface for all commands
    """
    __dna_data = DNA_Data()

    def execute(self, *args):
        raise

    def get_dna_data(self):
        return self.__dna_data
