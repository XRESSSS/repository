import library


def main():
    recipients = ['iprodauarbuzy@ukr.net']
    mail_body = 'Text from Odessa'
    mail_subject = "Hello"
    # attachment

    library.send_email(
        recipients=recipients,
        mail_body=mail_body,
        mail_subject=mail_subject
    )

if __name__ == '__main__':
    main()
