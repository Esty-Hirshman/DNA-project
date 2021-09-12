from command.command import Command


class Creation_commands(Command):
    """
    shared class for new and load command
    """
    __command = None

    def init_command(self, command):
        self.__command = command

    def check_command(self):
        """
        check command validation
        """
        try:
            3 <= len(self.__command) <= 4
        except ValueError:
            return "command not valid"
        if len(self.__command) == 4:
            if self.__command[2][0] != "@":
                return "name must start with '@'"

    def get_name(self):
        """
        get sequence name
        """
        if len(self.__command) == 4:
            return self.__command[2].replace("@", "")
        else:
            return None

    def execute(self, *args):
        try:
            if len(args) == 0:
                if len(self.__command) == 4:
                    dna_name = self.__command[2]
                else:
                    dna_name = super().get_dna_data().get_next_new_name("seq")
            else:
                dna_name = args[0]

            if len(self.__command) == 4:
                dna_name = self.__command[2].replace("@", "") if len(args) < 2 else args[0]
            dna_id = super().get_dna_data().get_next_id()
            dna_data = self.__command[1] if len(args) < 2 else args[1]
            try:
                super().get_dna_data().append_sequences(dna_data, dna_name, dna_id, self.__command[-1])
            except ValueError:
                return "DNA string not valid, must include only : A, G, C, T,a,g,c,t"
            if len(args) > 0 and len(dna_data) > 40:
                dna_data = args[1][0:32:] + "..." + args[1][-3::]
            return f"[{dna_id}] {dna_name}: {dna_data}"
        except:
            return "error in command"
