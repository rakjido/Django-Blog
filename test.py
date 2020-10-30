import logging
import hashlib
from random import random

logger = logging.getLogger(__name__)


# def add(a: int, b: int) -> int:
#     logger.info("add")
#     return a + b


# print(add(1, 2))


def get_hash(contents):
    blake = hashlib.blake2s(contents.encode("utf-8"), digest_size=4)
    return blake.hexdigest()


# random_value = str(random())
random_value = str(2 + 3421)
print(type(random_value))
print(random_value)
print(get_hash(random_value))