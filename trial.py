from custom_logging import CustomException, logger

if __name__ == '__main__':
    try:
        3/0
    except ZeroDivisionError as e:
        err = CustomException(original_exception=e)
    else:
        logger.info('All Good')