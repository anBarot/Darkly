
# How to get the flag

In the feedback page /index.php?page=feedback , you can insert scripts that can be executed in the name field.

"<script>alert("1")</script>"
Copying this into the name field gives the flag.

# How to prevent attack

You can prevent this attack with output encoding, converting the characters '<' or '>' for example.

# Documentation

https://owasp.org/www-community/attacks/xss/

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

