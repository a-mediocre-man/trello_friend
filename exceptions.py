class StatusCodeError(Exception):
    #raise when status code is not 200
    def __init__(self, status_code):
        self.status_code = status_code
        self.message = f"Got status code {status_code} instead of 200"
        super().__init__(self.message)
