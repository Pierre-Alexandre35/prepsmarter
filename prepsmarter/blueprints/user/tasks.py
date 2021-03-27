from utils.mail import send_template_message
from prepsmarter.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.

    :param email: E-mail address of the visitor
    :type user_id: str
    :param message: E-mail message
    :type user_id: str
    :return: None
    """
    print(message)
    ctx = {'email': email, 'message': message}
    send_template_message(email, message)
    return None
