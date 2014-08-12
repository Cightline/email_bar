import os
import configparser
from mailbox import MaildirMessage

config    = configparser.ConfigParser()
mailboxes = {}

config.read(os.path.expanduser('~/.config/email_bar.cfg'))

for mailbox in config.sections():
    mailboxes[mailbox] = 0



for mailbox in mailboxes:
    m = ['cur','new']
    
    base_path = '%s/INBOX' % (config.get(mailbox, 'path'))


    full_paths = ['%s/cur' % (base_path), '%s/new' % (base_path)]

    
    for path in full_paths:
        for mail in os.listdir(path):
            try:
                with open('%s/%s' % (path, mail)) as msg_file:
                    msg = MaildirMessage(msg_file.read())
                    if 'S' not in msg.get_flags():
                        mailboxes[mailbox] += 1

            except Exception as e:
                #print('[error] %s' % (e))
                pass

for mailbox in mailboxes.keys():
    print("%s unread: %s " % (mailbox, mailboxes[mailbox]), end="")



