# ESCAPE SEQUENCE CHARACTERS :

# \n for new line
print("Example: \\n for new line")
print("hello,\ni am bot")
print()

# \t for tab
print("Example: \\t for tab")
print("hello,\ti am bot")
print()

# \" for double quotes
print("Example: \\\" for double quotes")
print("hello, i am \"bot\"")
print()

# \' for single quotes
print("Example: \\' for single quotes")
print('It\'s a nice day!')
print()

# \\ for backslash
print("Example: \\\\ for backslash")
print("hello, i am \\bot\\")
print()

# \r for carriage return
print("Example: \\r for carriage return")
print("12345\rabc")  # 'abc45' because abc overwrites 123
print()

# \b for backspace
print("Example: \\b for backspace")
print("hello\b world")  # removes the 'o' before space
print()

# \f for form feed (less commonly used)
print("Example: \\f for form feed")
print("hello\fworld")
print()

# \v for vertical tab (may not be visible in all terminals)
print("Example: \\v for vertical tab")
print("hello\vworld")
print()

# \a for alert (bell sound)
print("Example: \\a for alert (bell sound)")
print("Hello\a")  # may beep in some terminals
print()

# Unicode examples:
print("Example: \\u for 16-bit Unicode character")
print("Greek Omega: \u03A9")
print()

print("Example: \\U for 32-bit Unicode character")
print("Smiling face: \U0001F600")
print()

print("Example: \\x for hex value")
print("Hex A: \x41")  # Prints 'A'
print()

print("Example: \\ooo for octal value")
print("Octal 101: \101")  # Prints 'A'


