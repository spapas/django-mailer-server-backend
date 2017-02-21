# django-mailer-server-backend
A django mail backend for mailer server (`https://github.com/spapas/mailer_server`)

Install it from git for now:

`pip install git+https://github.com/spapas/django-mailer-server-backend`

Use the following conf:

```
MAILER_SERVER_TOKEN = 'YOUR_MAILER_SERVER_TOKEN'
MAILER_SERVER_URL = 'http://MAILER_SERVER_URL/mail/api/send_mail/'
EMAIL_BACKEND = 'mailer_email_backend.MailerServerBackend'

```


