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
    - url

sheet (names eg base/ seasonal/ campaign x/ one off etc)
    *(All sheets override their project base sheet unless is base sheet)
    - id
    - owner
    - project (see `project.sheet` above)
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
    * have a `sheet.name` URL that supplies the minified direct to the base + only this `sheet`
    * have a obfuscated URL that supplies only the minified direct to this sheet ?? undecided on this
    * have a `project.name` URL that supplies the minified base + whatever is currently ranking `sheet`s
        - tags can also be used for eg, time++ or time-- relative or absolute *(to help with testing)

time
    - sheet (see `sheet.time` from above)
    - time (date + time)
    - time (duration (hours/days/weeks/months))
    - repeatType (enum)
    - repeatVal (int) (in # days)
    (repeatType should be based on the year kinda, eg:
        * repeat `NONE` - default,
        * repeat `DAY` of the month (x of 31),
        * repeat `WEEK` of the year (x of 52),
        * repeat `MONTH` of the year (x of 12),
        * repeat `YEAR` on the year (+x of year)
    With the user only being able to choose between each type not a combo!
        * all repeat times will be started from the day eg after midnight 00:01 am) 

TODO:
    - discount codes?
    - alpha/beta etc property
    - auto copy+paste for lazy people on the style sheet creation page
    - test page/view button ...?
    - better strap line than `cron jobs for styles`
    - 