import logging
import hashlib
from random import random

logger = logging.getLogger(__name__)


# def get_hash(contents):
#     blake = hashlib.blake2s(contents.encode("utf-8"), digest_size=6)
#     return blake.hexdigest()


def get_hash(id):
    # 임의의 값 3421
    idmix = str(id + 3421)
    blake = hashlib.blake2s(idmix.encode("utf-8"), digest_size=6)
    return blake.hexdigest()

