class ErrorCode(object):
    UNKNOWN_EXCEPTION = 10000
    VALIDATE_EXCEPTION = 10001

class SolarException(Exception):
    def __init__(self, code=ErrorCode.UNKNOWN_EXCEPTION, msg=None):
        self.code = code
        self.msg = msg

def build_result(body, exception=None):
    """
    exception 必须是 SolarException
    """
    if not exception: 
        return {
            'code': 0,
            'message': 'success',
            'body': body
        }
    else:
        return {
            'code': exception.code,
            'message': exception.msg,
            'body': ''
        }