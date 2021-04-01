def email(sendee_email="jbrcoleman@gmail.com",sentiment=1):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    if sentiment==1:
        content= "Thank you for the review! Glad you had a great time and hope to see you again!"
    else:
        content= "Sorry, that you didn't have a wonderful time. Please accept this promo code for 50% off your next experience! PROMO: SPRINGFUN2021"

    message = Mail(
        from_email=sendee_email,
        to_emails='jbrcoleman@gmail.com',
        subject='Coleman Corporation',
        html_content=f'<strong> {content} </strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e: # pylint: disable=W0703
        print(e.message) # pylint: disable=E1101

if __name__=='__main__':
    email()
