from passlib.hash import django_pbkdf2_sha256
hash = django_pbkdf2_sha256.hash("password")
print(hash)

correct_password = django_pbkdf2_sha256.verify('paswdasd', hash)
print(correct_password)