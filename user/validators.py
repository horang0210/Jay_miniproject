from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
import re
 
@deconstructible
class PasswordValidator:
    
    message = "비밀번호는 8자리 이상이며, 영문과 숫자를 1개 이상 포함해야 합니다."
    code = "invalid"
    password_regex = '^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
        
    def __init__(self, message=None, code=None):
        if message is not None:
            self.message=message
            
        if code is not None:
            self.code=code
    
    
    def __call__(self, value): 
        try:
            if not value:
                raise ValidationError(self.message, code=self.code, params={'value':value})
            
            if not re.fullmatch(self.password_regex, value):
                raise ValidationError(self.message, code=self.code, params={'value':value})
            
        except ValidationError as e:
            raise ValidationError(str(e))
    
        
    def __eq__(self, other):
        return(
            isinstance(other, PasswordValidator) and
            (self.message == other.message) and
            (self.code == other.code)
        )
    