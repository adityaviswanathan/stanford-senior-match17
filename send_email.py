#!/usr/bin/env python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sender_details import SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD
from recipient_details import HTML_TEMPLATE, SUBJECT, RECIPIENTS, PLAIN_TEXT_FALLBACK

for recipient in RECIPIENTS:
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = SUBJECT
	msg['From'] = SENDER_EMAIL_ADDRESS
	msg['To'] = recipient

	# Create the body of the message (a plain-text and an HTML version).
	text = PLAIN_TEXT_FALLBACK
	html = HTML_TEMPLATE

	# Record the MIME types of both parts - text/plain and text/html.
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	msg.attach(part1)
	msg.attach(part2)

	# Send the message via local SMTP server.
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	s.login(SENDER_EMAIL_ADDRESS, SENDER_EMAIL_PASSWORD)
	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	s.sendmail(SENDER_EMAIL_ADDRESS, recipient, msg.as_string())
	print 'Sent email to',recipient
	s.quit()