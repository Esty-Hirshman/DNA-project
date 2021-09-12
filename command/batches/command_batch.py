from data.batch_data import Batch_Data


class Command_Batch:
    """
    interface for batch commands
    """
    __batch_data = Batch_Data()

    def execute(self, *args):
        raise

    def get_batch_data(self):
        return self.__batch_data
