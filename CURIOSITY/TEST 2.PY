import pywhatkit as pwk

phone_number = "+917892212204"
message = "hello"

# Sends instantly (with minimal wait)
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True, close_time=3)
