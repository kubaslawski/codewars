"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".
"""
from datetime import datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    date_format = "%B %d, %Y"
    exp_date = datetime.strptime(expiration_date, date_format)
    curr_date = datetime.strptime(current_date, date_format)
    return exp_date >= curr_date and entered_code is correct_code


check_coupon(2, '2','September 5, 2014','September 25, 2014')