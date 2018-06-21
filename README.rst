django-mailer-server-backend
----------------------------

A django mail backend for mailer server (https://github.com/spapas/mailer_server)

Install it from pip:

``pip install django-mailer-server-backend``

or the latest version from git:

``pip install git+https://github.com/spapas/django-mailer-server-backend``

Then use the following conf in your django app:

```
MAILER_SERVER_TOKEN = 'YOUR_MAILER_SERVER_TOKEN'
MAILER_SERVER_URL = 'http://MAILER_SERVER_URL/mail/api/send_mail/'
EMAIL_BACKEND = 'mailer_email_backend.MailerServerBackend'
```


