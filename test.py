import logging

logger = logging.getLogger(__name__)


def add(a: int, b: int) -> int:
    logger.info("add")
    return a + b


print(add(1, 2))
