from rest_framework.exceptions import ValidationError


def validate_four_digit_year(value):
    if len(str(value)) != 4:
        raise ValidationError("Год должен быть четырёхзначным числом.")


def validate_year_range(data):
    start_year = data["start_year"]
    end_year = data["end_year"]
    if start_year > end_year:
        raise ValidationError("Год начала выпуска должен быть меньше года окончания выпуска.")
