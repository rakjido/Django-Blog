import six
import logging

from django.contrib.auth.tokens import PasswordResetTokenGenerator

logger = logging.getLogger('blog')

class TokenGenerator(PasswordResetTokenGenerator):
    logger.info("TokenGenerator")
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.id) + six.text_type(timestamp) + six.text_type(user.is_active)


account_activation_token = TokenGenerator()
