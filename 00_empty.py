def save_email(email):
    return email.lower().strip("_- ")


mail = "_supPort@hexlet.IO__  -"
print(save_email(mail))


