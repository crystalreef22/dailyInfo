#!/bin/python3
from provider import infotext, cDay
import time
import subprocess


subprocess.run(["termux-notification", "-t", "d"+str(cDay), "-c", infotext, "--icon", "filter_"+str(cDay), "--id", "8363", "--ongoing", "--button1", "dismiss", "--button1-action", "termux-notification-remove 8363"])

'''
age: termux-notification [options]
Display a system notification. Content text is specified using -c/--content or read from stdin.                                                                                 Please read --help-actions for help with action arguments.                                --action action          action to execute when pressing the notification
  --alert-once             do not alert when the notification is edited
  --button1 text           text to show on the first notification button
  --button1-action action  action to execute on the first notification button
  --button2 text           text to show on the second notification button                 --button2-action action  action to execute on the second notification button
  --button3 text           text to show on the third notification button
  --button3-action action  action to execute on the third notification button
  -c/--content content     content to show in the notification. Will take
                           precedence over stdin. If content is not passed as
                           an argument or with stdin, then there will be a 3s delay.
  --group group            notification group (notifications with the same
                           group are shown together)
  -h/--help                show this help
  --help-actions           show the help for actions
  -i/--id id               notification id (will overwrite any previous notification
                           with the same id)
  --icon icon-name         set the icon that shows up in the status bar. View
                           available icons at https://material.io/resources/icons/
                           (default icon: event_note)
  --image-path path        absolute path to an image which will be shown in the
                           notification
  --led-color rrggbb       color of the blinking led as RRGGBB (default: none)
  --led-off milliseconds   number of milliseconds for the LED to be off while
                           it's flashing (default: 800)
  --led-on milliseconds    number of milliseconds for the LED to be on while
                           it's flashing (default: 800)
  --on-delete action       action to execute when the the notification is cleared
  --ongoing                pin the notification
  --priority prio          notification priority (high/low/max/min/default)
  --sound                  play a sound with the notification
  -t/--title title         notification title to show
  --vibrate pattern        vibrate pattern, comma separated as in 500,1000,200
  --type type              notification style to use (default/media)
Media actions (available with --type "media"):
  --media-next             action to execute on the media-next button
  --media-pause            action to execute on the media-pause button
  --media-play             action to execute on the media-play button
  --media-previous         action to execute on the media-previous button
'''
