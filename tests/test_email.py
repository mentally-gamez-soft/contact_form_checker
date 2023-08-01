import unittest

from core.email import Email


class TestEmail(unittest.TestCase):

    def setUp(self) -> None:
        self.email = Email(from_recipient='unknown_user@jungle.fr', subject='This is a test message', body='This message is brought to you by SquareSpace. Viva la fotogragfia y viva espania.')

    def test_email_validity(self):
        self.assertTrue(self.email.is_valid_email()['status'], self.email.is_valid_email()['info'])

    def test_email_has_subject(self):
        self.assertTrue(self.email.has_subject(),'The title of the email is not filled in!')

    def test_email_has_body(self):
        self.assertTrue(self.email.has_body(), 'The body of the email is not filled in!')

    def test_email_body_length(self):
        self.assertTrue(len(self.email.get_body()) >= 30)

    def test_email_title_length(self):
        self.assertTrue(len(self.email.get_subject()) >= 15)