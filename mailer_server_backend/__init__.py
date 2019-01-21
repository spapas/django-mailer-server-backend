from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen, Request

def get_dict_from_message(em):
    d = {}
    d['subject'] = em.subject
    d['body'] = em.body
    d['mail_from'] = em.from_email
    d['cc'] = ','.join(em.cc)
    d['bcc'] = ','.join(em.bcc)
    d['mail_to'] =','.join(em.to)
    d['reply_to'] = ','.join(em.reply_to)
    d['body_type'] = em.content_subtype
    return d


class MailerServerBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        send_count = 0
        for em in email_messages:
            emd = get_dict_from_message(em)
            data = json.dumps(emd)
            req = Request(settings.MAILER_SERVER_URL)
            req.add_header('Content-Type', 'application/json')
            req.add_header('Authorization', 'Token {0}'.format(settings.MAILER_SERVER_TOKEN))
            resp = urlopen(req, data)
            content = resp.read()
            if resp.code == 200:
                send_count+=1
        return send_count
