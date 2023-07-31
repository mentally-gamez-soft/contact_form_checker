import unittest

from core.email import Email


class TestEmail(unittest.TestCase):

    def setUp(self) -> None:
        self.email = Email(from_recipient='unknown_user@jungle.fr', subject='test_email', body='This is a test message.')

    def test_email_validity(self):
        self.assertTrue(self.email.is_valid_email()['status'], self.email.is_valid_email()['info'])

    def test_email_has_subject(self):
        self.assertTrue(self.email.has_subject(),'The title of the email is not filled in!')

    def test_email_has_body(self):
        self.assertTrue(self.email.has_body(), 'The body of the email is not filled in!')