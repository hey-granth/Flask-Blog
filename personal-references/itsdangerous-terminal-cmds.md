# itsdangerous Terminal Commands

- python3
- from itsdangerous import URLSafeTimedSerializer as Serializer
- s = Serializer('secret')
- token = s.dumps({'user_id':1})
- token = s.loads(token, 30)
> It is used to create a serializer object `s` with a `secret key` and a time limit of 30 seconds. And `token` is used to dump and load the data.
