from jsonrpc.exceptions import JSONRPCDispatchException


class RegionError(JSONRPCDispatchException):
    def __init__(self):
        super().__init__(-31989, '验证错误')
