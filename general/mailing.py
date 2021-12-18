from django.core.mail import send_mail


def send_mails(title, body, toWho):

    send_mail(title,
              body,
              'djangoProjectWeb@gmail.com',
              toWho,
              fail_silently=False)
    return
