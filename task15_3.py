import re


def F(s):
    s1 = r"\+7\(812\)\-\d{3}\-\d{2}-\d{2}|\+7\(921\)\-\d{3}-\d{2}-\d{2}|\+7\(812\)\-\d{3}\-\d{4}|\+7\(921\)\-\d{3}\-\d{4}"
    phone = re.findall(s1, s)
    return phone


check = '+7(812)-234-34-55tgmjk+7(921)-234-34-55kjhfds+7(812)-234-3455tgmjk+7(921)-234-3455kjhfdr'

print(F(check))