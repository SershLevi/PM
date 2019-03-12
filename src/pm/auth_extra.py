from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class SpecialCharactersInclusionValidator:
    DEFAULT_SPECIAL_CHARACTERS = ('!', '@', '#', '$', '%', '^',
                                  '&', '*', '(', ')', '_', '+',
                                  '=', '-', '/', '\\', '|', '.',
                                  ',', '>', '<', "\"", '\'', ';',
                                  ':')

    def __init__(self, special_chars=DEFAULT_SPECIAL_CHARACTERS):
        self.special_chars = special_chars

    def validate(self, password, user=None):
        has_special_chars = False
        for char in self.special_chars:
            if char in password:
                has_special_chars = True
                break
        if not has_special_chars:
            raise ValidationError(
                self.get_help_text(pronoun="this"),
                code="password_missing_special_chars"
            )

    def get_help_text(self, pronoun="your"):
        return _(f"{pronoun.capitalize()} password must contain at "
                 f"least one of the following special characters: "
                 f"{' '.join(self.special_chars)}")
