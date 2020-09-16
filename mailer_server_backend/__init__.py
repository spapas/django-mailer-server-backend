from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
import json
try:
    # For Python 3.0 and later
    from urllib.request import urlopen, Request
    from urllib.parse import urlparse
    import urllib
    import http.client
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

# Code from https://stackoverflow.com/a/681182/119071
def encode_multipart_formdata(fields, files):
    LIMIT = b'----------lImIt_of_THE_fIle_eW_$'
    CRLF = b'\r\n'
    L = []
    for (key, value) in fields.items():
        L.append(b'--' + LIMIT)
        L.append(b'Content-Disposition: form-data; name="%s"' % key.encode())
        L.append(b'')
        L.append(value.encode())
    for (filename, content, content_type) in files:
        L.append(b'--' + LIMIT)
        L.append(b'Content-Disposition: form-data; name="%s"; filename="%s"' % (b"attachment", filename.encode()))
        L.append(b'Content-Type: %s' % content_type.encode())
        L.append(b'')
        if isinstance(content, bytes):
            L.append(content)
        else:
            L.append(content.encode())

    L.append(b'--' + LIMIT + b'--')
    L.append(b'')
    body = CRLF.join(L)

    content_type = 'multipart/form-data; boundary=%s' % LIMIT.decode()
    return content_type, body


class MailerServerBackend(BaseEmailBackend):
    def send_messages(self, email_messages):

        send_count = 0
        for em in email_messages:
            emd = get_dict_from_message(em)

            if len(em.attachments) > 0:
                # For attachments we need to use the http.client
                # Works only on python 3
                o = urlparse(settings.MAILER_SERVER_URL)

                ct, data = encode_multipart_formdata(emd, em.attachments)

                h = http.client.HTTPConnection(o.netloc.split(':')[0], o.port)
                h.putrequest('POST', o.path)
                h.putheader('content-type', ct)
                h.putheader('content-length', str(len(data)))
                h.putheader('Authorization', 'Token {0}'.format(settings.MAILER_SERVER_TOKEN))
                h.endheaders()

                h.send(data)
                resp = h.getresponse()
                status = resp.status

            else:
                req = Request(settings.MAILER_SERVER_URL)
                req.add_header('Content-Type', 'application/json')
                req.add_header('Authorization', 'Token {0}'.format(settings.MAILER_SERVER_TOKEN))
                data = json.dumps(emd)
                req.add_header('Content-Type', 'application/json')

                try:
                    resp = urlopen(req, data.encode('utf-8'))
                except TypeError:
                    resp = urlopen(req, data)

                content = resp.read()
                status = resp.code
            if status == 200:
                send_count+=1
        return send_count
