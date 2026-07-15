import logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="logs.log",
        filemode="a",
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )