from datetime import datetime

class BaseDataTransfer(object):
    def __init__(self, **kwargs):
        for field in ('message', 'timestamp'):
            setattr(self, field, kwargs.get(field, datetime.now() if(field == 'timestamp') else None))
