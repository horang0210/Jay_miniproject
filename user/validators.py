from django.core.exceptions import ValidationError
# from django.contrib.auth.password_validation import validate_password
# import re
 
 
class CustomPasswordValidator:
    # def __call__(self, value): 
    #     try:
    #         validate_password(value)
    #     except ValidationError as e:
    #         raise ValidationError(str(e))
 
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                '비밀번호에는 숫자가 포함되어 있어야 합니다.'
            )
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                '비밀번호에는 영문이 포함되어 있어야 합니다.'
            )
        if len(password) < 8 :
            raise ValidationError(
                '비밀번호는 8자리 이상으로 구성되어야 합니다.'
            )
 
    def get_help_text(self): 
        return "비밀번호는 8자리 이상이며 영문, 숫자를 1개 이상 포함해야 합니다."
