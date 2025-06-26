# format specifiers = {:flags} forma a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number)  = allocate that many spaces
# :03        = allocate and zero pad that many spaces
# :<         = left justify
# :>         = right justify
# :^         = center align
# :+         = use a plug sign to indicate positive values
# :=         = place sign to leftmost position
# :          = insert a space before positive numbers
# :,         = comma seperator

pi = 3020.14156
value = -9120.76

# Decimal Spaces

print(f"round to that many decimal places: {pi:.1f}")
print(f"round to that many decimal places: {value:.1f}")
print()

# Allocate Spaces

print(f"allocate that many spaces: {pi:10}")
print(f"allocate that many spaces: {value:10}")
print()

# Zero padding spaces

print(f"allocate and zero pad that many spaces: {pi:010}")
print(f"allocate and zero pad that many spaces: {value:010}")
print()

# Left Justify
# Highlight the output and check for justification

print(f"left justify: {pi:<10}")
print(f"left justify: {value:<10}")
print()

# Right Justify
# Highlight the output and check for justification

print(f"right justify: {pi:>10}")
print(f"right justify: {value:>10}")
print()

# Center Align
# Highlight the output and check for justification

print(f"center align: {pi:^10}")
print(f"center align: {value:^10}")
print()

# + Sign in output for positive numbers
# Negative numbers stay -

print(f"use a plug sign to indicate positive values: {pi:+}")
print(f"Nothing Changes: {value:+}")
print()

# Insert space for positive numbers

print(f"Insert space for positive numbers: {pi: }")
print(f"Nothing changes: {value:+}")
print()

# Comma Seperator
# 1000 Seperator, i.e., the comma would be at 1000th place

print(f"Comma Seperator: {pi:,}")
print(f"Comma Seperator: {value:,}")
print()

