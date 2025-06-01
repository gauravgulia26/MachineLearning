import sys, traceback, logging, coloredlogs

FORMAT = "%(asctime)s - %(message)s"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(filename="logs.log", mode="w")
file_formatter = logging.Formatter(fmt=FORMAT)
file_handler.setFormatter(fmt=file_formatter)
logger.addHandler(file_handler)

coloredlogs.install(logger=logger, fmt=FORMAT, level=logging.INFO)


class CustomException(Exception):
    def __init__(self, original_exception: Exception):
        if not isinstance(original_exception, Exception):
            raise ValueError("Must be a exception")
        _, _, tb = sys.exc_info()
        tb_info = traceback.extract_tb(tb)[-1]
        filename = tb_info.filename
        line_number = tb_info.lineno
        error_type = type(original_exception).__name__
        error_message = str(original_exception)

        self.message = (
            f"Exception Type: {error_type}\n"
            f"File Name: {filename}\n"
            f"Line Number: {line_number}\n"
            f"Error Message: {error_message}"
        )

        self.__log_exception()

    def __log_exception(self):
        logger.error(self.message)

if __name__ == '__main__':
    try:
        3/0
    except ZeroDivisionError as e:
        err = CustomException(original_exception=e)
    else:
        logger.info('All Good')