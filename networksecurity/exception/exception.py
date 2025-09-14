import sys
import logging
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message
        self.error_detail = error_detail
        self.line_number = error_detail.exc_info()[2].tb_lineno
        self.file_name = error_detail.exc_info()[2].tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in Python script: {self.file_name} at line {self.line_number} with message: {self.error_message}"