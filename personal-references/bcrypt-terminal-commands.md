# Bcrypt Terminal Commands

- python3
- from flask_bcrypt import Bcrypt
- bcrypt = Bcrypt()
- bcrypt.generate_password_hash('testing')
- hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
- bcrypt.check_password_hash(hashed_pw, 'password')
- bcrypt.check_password_hash(hashed_pw, 'testing')
- 