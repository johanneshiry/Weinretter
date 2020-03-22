import requests

def verify_captcha(token):
    r = requests.post('https://www.google.com/recaptcha/api/siteverify',
                  {'response': token, 'secret': '6Le3Kp4UAAAAAMkPcidI-o8gDu807ZnqzLr9Axqb'})
    return r.json()["success"]
