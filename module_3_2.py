def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
	domen_mail = ['.com', '.ru', '.net']
	if (('@' not in sender or '@' not in recipient) or
		(recipient[-4:] not in domen_mail and recipient[-3:] not in domen_mail) or
		(sender[-4:] not in domen_mail and sender[-3:] not in domen_mail)):
		print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
	elif sender == recipient:
		print('Нельзя отправить письмо самому себе!')
	elif sender == 'university.help@gmail.com':
		print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
	else:
		print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
	sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')