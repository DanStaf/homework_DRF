from rest_framework import serializers


class TextValidator:

    def __init__(self, field, correct_text):
        self.field = field
        self.correct_text = correct_text

    def __call__(self, value):
        if value is None or len(value) == 0:
            result = True
        else:
            index = value.lower().find(self.correct_text.lower())
            result = (index != -1)

        if not result:
            message = f"Допустимы только ссылки на {self.correct_text}"
            raise serializers.ValidationError(message)
