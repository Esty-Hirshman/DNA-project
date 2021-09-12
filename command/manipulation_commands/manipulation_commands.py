from command.command import Command


class Manipulation_Command(Command):
    """
    shared class to manipulation commands
    """
    __command = None
    __dna_to_change = None

    def init_command(self, command):
        self.__command = command

    def check_command(self):
        """
        check command validation
        """
        if self.__command[1][0] != '#' and self.__command[1][0] != '@':
            return "invalid command"
        if self.__command[-1] == ":":
            return "command not valid, mast finish with @name or @@"

    def execute(self, *args):
        """
        get seq to manipulate
        """
        if self.__command[1][0] == "#":
            self.__dna_to_change = self.__command[1].replace("#", "")
        else:
            self.__dna_to_change = self.__command[1].replace("@", "")
        to_change = super().get_dna_data().get_sequence_by_id_or_name(self.__command[1])
        return to_change

    def change_given_seq(self, new_seq, dna_to_slice,new_name_to_change=""):
        """
        change given seq after manipulate according to name in command
        """

        # if name not in command use seq name
        if ':' not in self.__command:
            new_name = dna_to_slice.get_dna_name()
            self.__dna_to_change = dna_to_slice.get_dna_id()
        # if name given as '@@' use random name as defined with '_ri' or '_si'
        elif "@@" in self.__command:
            name = dna_to_slice.get_dna_name()
            new_name = super().get_dna_data().get_next_new_name(name, new_name_to_change)
            self.__dna_to_change = super().get_dna_data().get_next_id()
        # if new name is given use new name after manipulate
        else:
            self.__command[-1].replace("@", "")
            self.__dna_to_change = super().get_dna_data().get_next_id()
            new_name = self.__command[-1]
        # Adds the seq after manipulate by overriding the old one if name is the same
        super().get_dna_data().append_sequences(new_seq, new_name, self.__dna_to_change,"*")
        return f"[{self.__dna_to_change}] {new_name} : {new_seq}"
