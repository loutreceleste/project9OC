from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    @staticmethod
    def validate(password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')

    @staticmethod
    def get_help_text():
        return 'Votre mot de passe doit contenir au moins une lettre.'