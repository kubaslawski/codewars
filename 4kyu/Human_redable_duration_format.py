"""
DESCRIPTION:
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
"""

def format_duration(seconds):
    y, seconds = divmod(seconds, 31536000)
    d, seconds = divmod(seconds, 86400)
    h, seconds = divmod(seconds, 3600)
    m, s = divmod(seconds, 60)

    y_unit = "year" if y == 1 else "years"
    d_unit = "day" if d == 1 else "days"
    h_unit = "hour" if h == 1 else "hours"
    m_unit = "minute" if m == 1 else "minutes"
    s_unit = "second" if s == 1 else "seconds"

    time_units = []
    if y > 0:
        time_units.append(f"{y} {y_unit}")
    if d > 0:
        time_units.append(f"{d} {d_unit}")
    if h > 0:
        time_units.append(f"{h} {h_unit}")
    if m > 0:
        time_units.append(f"{m} {m_unit}")
    if s > 0:
        time_units.append(f"{s} {s_unit}")

    if len(time_units) > 1:
        time_string = ", ".join(time_units[:-1]) + " and " + time_units[-1]
    else:
        time_string = time_units[0]
    return time_string