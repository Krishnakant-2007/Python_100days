import datetime      #datetime is a module

# a = datetime.now()
# print(a)    #This throws ERROR..., Because, "datetime refers to the module", not the "datetime class" inside the module.

#correct method-1..
a = datetime.datetime.now()
print(a)    #Gives current date and time...    Think like: datetime(module) --> datetime(class) --> now()(method)

#correct method-2..
from datetime import datetime

a = datetime.now()
print(a)   #Gives current datetime

#What is "strftime()"?

# "strftime()" means:
# String Time format

# It converts a date/time object into a formatted string

#SYNTAX:
#datetime_object.strftime("format")

#EXAPMLE
from datetime import datetime

now = datetime.now()
print(now.strftime("%H:%M:%S:%p"))     #OUTPUT is like 15:17:42      %H -> Hour; %M -> Minute; %S -> Second

#IMPORTANT FORMAT CODES


#  %H    --> 24-hour-format
#  %I    --> 12-hour-format
#  %M    --> Minute
#  %S    --> Second
#  %p    --> AM/PM
#  %m    --> Month
#  %d    --> Date
#  %Y    --> 4-digit year             (2026)
#  %y    --> 2-digit year             (26)
#  %A    --> Full weekday name        (Monday)
#  %a    --> Short weekday name       (Mon)
#  %B    --> Full month name          (September)
#  %b;%h --> Short month name         (Sep)



#FORMATTING A DATE....
from datetime import datetime
now = datetime.now()

print(now.strftime("%d-%m-%Y"))      #OUTPUT is like 05-09-2026
print(now.strftime("%d-%B-%Y"))      #OUTPUT is like 05-September-2026
print(now.strftime("%d-%b-%Y"))      #OUTPUT is like 05-Sep-2026
print(now.strftime("%A,%d-%b-%Y"))   #OUTPUT is like Saturday,05-Sep-2026
print(now.strftime("%a,%d-%b-%Y"))   #OUTPUT is like Sat,05-Sep-2026


#FORMATTING DATE AND TIME TOGETHER....
from datetime import datetime

now = datetime.now()
print(now.strftime("%A,%d-%b-%Y  %H:%M:%S%p"))      #OUTPUT is like; Saturday,05-Sep-2026  16:28:32
