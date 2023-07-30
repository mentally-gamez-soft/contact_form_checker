from email_validator import EmailNotValidError, validate_email


class Email():

    def __init__(self, **kwargs) -> None:
        self.subject = kwargs.get('subject')
        self.body = kwargs.get('body')
        self.from_recipient = kwargs.get('from_recipient')

    def is_valid_email(self) -> dict:
        result = {}
        result['status'] = True
        result['info'] = ''

        try:
            emailinfo = validate_email(self.from_recipient, check_deliverability=True)
            self.from_recipient = emailinfo.normalized
            result['info'] = self.from_recipient
        except EmailNotValidError as e:
            result['status'] = False
            result['info'] = str(e)
        
        return result

    def has_subject(self):
        return bool(self.subject)
    
    def has_body(self) -> bool:
        return bool(self.body)
    
email = Email(from_recipient='unknOwn_user@JUNGL.fr', subject='test_email', body='This is a test message.')

print(email.is_valid_email())
