from command import *
from command.manipulation_commands import *
from command.management_commands import *
from command.sequence_analysis_commands import *
from command.control_commands import *
from command import batches


class Factory:
    """
    Holds all commands in a dictionary and returns an object of command according to the MB received
    """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not Factory.__instance:
            Factory.__instance = object.__new__(cls)
        return Factory.__instance

    def __init__(self):
        self.__command_dict = {
            "new": Command_New,
            "load": Command_Load,
            "dup": Command_Dup,
            "slice": Command_Slice,
            "replace": Command_Replace,
            "del": Command_Del,
            "save": Command_Save,
            "len": Command_Len,
            "find": Command_Find,
            "count": Command_Count,
            "findall": Command_Findall,
            "quit": Command_Quit,
            "list": Command_List,
            "batch": batches.Create_Batch,
            "run": batches.Run_Batch_Command,
            "batchlist": batches.Command_Batchlist,
            "batchshow": batches.Command_Batchshow,
            "batchsave": batches.Command_Batchsave,
            "batchload": batches.Command_Batchload

        }

    def get_command_type(self, type):
        """
        get the required command
        :param type: command type
        """
        return self.__command_dict[type]()
