from command.management_commands.management_commands import Management_Commands


class Command_Save(Management_Commands):
    """
    save seq to file' change status to '-'
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_Save.__instance:
            Command_Save.__instance = object.__new__(cls)
        return Command_Save.__instance

    def execute(self, command):
        super().init_command(command)
        error = super().check_command(command)
        if error: return error
        dna_to_save = super().get_seq_to_manage(command)
        file_name = f"{dna_to_save.get_dna_name()}.rawdna" if len(command) == 2 else command[2]
        try:
            with open(file_name, "a") as file_to_save:
                file_to_save.write(
                    f"{dna_to_save.get_dna()}")
                super().get_dna_data().set_status(dna_to_save.get_dna_id(),"-")
                return f"Saved: [{dna_to_save.get_dna_id()}] {dna_to_save.get_dna_name()}: {dna_to_save.get_dna()}"
        except FileNotFoundError:
            return "file not found"
