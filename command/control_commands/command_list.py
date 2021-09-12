from command import Command


class Command_List(Command):
    """
    get all sequences in data with the status, id, name and seq string
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Command_List.__instance:
            Command_List.__instance = object.__new__(cls)
        return Command_List.__instance

    def execute(self, command):
        try:
            command == ["list"]
        except:
            return "invalid list command"
        return "\n".join(super().get_dna_data().get_all_sequences())
