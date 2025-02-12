from mailer import Mailer
from mailer import Message
from account_module import models as user
message = Message(From='"مجله آموزشی راکت 👻" <info@localhost:3000>',
                  To=user.User.email,
                  charset="utf-8")
message.Subject = "An HTML Email"
message.Html = """This email uses <strong>HTML</strong>!"""
message.Body = """This is alternate text."""

sender = Mailer('smtp.example.com')
sender.send(message)