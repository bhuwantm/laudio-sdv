from sdv import Metadata


class BaseSDV:

    def __init__(self, metadata: Metadata):
        self.metadata = metadata

    @staticmethod
    def _get_fields_metadata():
        return NotImplementedError

    def get_df_and_metadata(self):
        return NotImplementedError
