import requests
from schematics.exceptions import ValidationError


def validate_captcha(token):
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                      {'response': token, 'secret': '6Le3Kp4UAAAAAMkPcidI-o8gDu807ZnqzLr9Axqb'})
    json = r.json()

    if not json["success"] or json["score"] < 0.5:
        raise ValidationError('Captcha invalid')
