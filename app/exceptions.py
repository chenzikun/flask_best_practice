
class DataMissingError(Exception):
    def __init__(self, err="您访问的数据不存在"):
        super(DataMissingError, self).__init__(err)

