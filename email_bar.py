#!/bin/python

import os
import configparser
import argparse

from mailbox import MaildirMessage

config    = configparser.ConfigParser()
config_mailboxes = {}

config.read(os.path.expanduser('~/.config/email_bar.cfg'))

parser = argparse.ArgumentParser()
parser.add_argument('--only',     help='only check specified mailbox', action='store')
parser.add_argument('--no-title', help='do not display the title', action='store_true')

args = parser.parse_args()

if args.only:
    config_mailboxes[args.only] = 0

# Else read through the config and check all of the mailboxes
else:
    for mailbox in config.sections():
        config_mailboxes[mailbox] = 0


def check_unread(mailboxes):
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
                            config_mailboxes[mailbox] += 1

                except Exception as e:
                    #print('[error] %s' % (e))
                    pass

check_unread(config_mailboxes)

for mailbox in config_mailboxes.keys():
    if args.no_title:
        print(config_mailboxes[mailbox])

    
    else:
        print("%s: %s " % (mailbox, config_mailboxes[mailbox]), end="")



