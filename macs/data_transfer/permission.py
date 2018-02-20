from .base_data_transfer import BaseDataTransfer


class Permission(BaseDataTransfer):
    def __init__(self, **kwargs):
        super().__init__()
        for field in ('machine', 'member', 'permission'):
            setattr(self, field, kwargs.get(field, None))

