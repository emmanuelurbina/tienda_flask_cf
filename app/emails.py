from threading import Thread
from flask_mail import Message
from flask import current_app, render_template



# def confirmar_compra(mail, usuario, libro):
#     try:
#         message = Message('Confirmación de compra de libro',
#                           sender=current_app.config['MAIL_USERNAME'],
#                           recipients=['emmanuel.lucio.urbina@gmail.com'] )
#         message.html = render_template(
#             'emails/confirma_compra.html', usuario=usuario, libro=libro)
#         mail.send(message)
#     except Exception as ex:
#         raise Exception(ex)


def confirmar_compra(app, mail, usuario, libro):
    try:
        message = Message('Confirmación de compra de libro',
                          sender=current_app.config['MAIL_USERNAME'],
                          recipients=['emmanuel.lucio.urbina@gmail.com'] )
        message.html = render_template(
            'emails/confirma_compra.html', usuario=usuario, libro=libro)
        thread = Thread(target=envio_async_mail, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)


def envio_async_mail(app, mail, message):
    with app.app_context():
        mail.send(message)