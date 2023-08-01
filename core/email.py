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
    
    def get_body(self) -> str:
        return self.body
    
    def has_valid_body_length(self) -> str:
        return len(self.body) >= 30

    def get_subject(self) -> str:
        return self.subject
    
    def has_valid_subject_length(self) -> str:
        return len(self.body) >= 15

    def has_subject(self) -> bool:
        return bool(self.subject)
    
    def has_body(self) -> bool:
        return bool(self.body)