from command.creation_commands.creation_commands import Creation_commands
import os


class Command_Load(Creation_commands):
    """
    load seq from file to data
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Load.__instance:
            Command_Load.__instance = object.__new__(cls)
        return Command_Load\
            .__instance

    def execute(self, command):
        command.append("-")
        super().init_command(command)
        error = super().check_command()
        if error: return error
        if '.' not in command[1]:
            command[1] += '.rawdna'
        dna_name = super().get_name()
        try:
            with open(command[1], "r") as dna_file:
                dna_data = dna_file.readline()
                # if name not given take the file name
                if not dna_name:
                    dna_name = os.path.splitext(os.path.basename(command[1]))[0]
                return super().execute(dna_name, dna_data)
        except FileNotFoundError as file_error:
            return str(file_error)
