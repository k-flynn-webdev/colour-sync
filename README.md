# colour-sync
A colour service to help with the ever-changing branding ..


A website service for keeping track of all your colours and brands colours. 
Super simple and built for maintaining brand campaigns or helping out small web 
developers keep up with all their sites colours and changes.

This all depends on how easy it is to use a url for a colour in webdev in the build process

Super simple and secure urls, plus tags for:
Latest version
Indefinite secure version
Rgb or cmyk or Hsl etc
Older versions by date (absolute or relative)
Older versions by changes (relative)
Seasonal changing version (eg winter summer)
Holiday version (eg Xmas Easter etc)
Campaign/tag versions
Campaigns that override the latest for a period of time...

Everything should be built with a super simple tagging system that shows kind of like a game what would happen.

Pay super small amount eg €2 a year. I’m just collecting colours and not much data.

user
    - id
    - meta

project
    - id
    - owner (user)
    - user (update)(many)
    - user (read)(many)
    - name
    - meta
    - sheet (many) *(a base sheet will always be created with the lowest ranking)

sheet (names eg base/ seasonal/ campaign x/ one off etc)
    *(All sheets override their project base sheet unless is base sheet)
    - id
    - owner
    - users (update)(many)
    - users (read)(many)
    - name
    - meta
    - time (many) ??
    - importance/ranking
    - data
    - url

data
    - data blob of what styles they want
    - type { scss : css : built }

url 
    - api { css : scss }
    - non-api { css }
    - absolute { css : scss } *(ignores time/ranking)
    - relative { css : scss } *(relative time (hours/days/weeks/months))

time
    - time (date + time)
    - time (duration (hours/days/weeks/months))
    - isRepeat (cron like? (Year, Month, DayOfMonth)) *(this needs more thought)

