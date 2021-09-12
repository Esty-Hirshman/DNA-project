from command.command import Command


class Management_Commands(Command):
    """
    shared class for management commands
    """
    __command = None

    def init_command(self, command):
        self.__command = command

    def check_command(self, command):
        """
        check command validation
        """
        if not 2 <= len(command) <= 3:
            return "command not valid, missing or to mach args"
        if command[1][0] not in ["#", "@"]:
            return "command not valid, seq must start with '@' or '#'"

    def get_seq_to_manage(self, command):
        """
        get seq to manage
        """
        return super().get_dna_data().get_sequence_by_id_or_name(command[1])
