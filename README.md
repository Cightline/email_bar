email_bar
=========

Tool to display unread emails from maildir format to conky, i3status, etc..

Example usage:
```email_bar.py --only my_account_name```

Account name is specified in the configuration, which has the "path" option.
```
[my_account_name]
path = /home/user/.email/account/Maildir/INBOX
```

The configuration should be kept at ```~/.config/email_bar.cfg```



Installation:
```
./install.sh
```
