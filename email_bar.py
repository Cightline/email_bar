#!/bin/python

import os
import configparser
import argparse

from mailbox import MaildirMessage
from mailbox import MMDFMessage
from mailbox import Maildir

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

        maildir = Maildir(config.get(mailbox, 'path'))

        for mail in maildir:
            if 'S' not in mail.get_flags():
                config_mailboxes[mailbox] += 1


check_unread(config_mailboxes)

for mailbox in config_mailboxes.keys():
    if args.no_title:
        print(config_mailboxes[mailbox])

    
    else:
        print("%s: %s " % (mailbox, config_mailboxes[mailbox]), end="")



