
# How to get the flag

There is a hidden field in the submit element of the recover password /?page=recover:
```
<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
```
Changing the value of the mail will get you the flag.

# How to prevent attack

You can store the mail info in a database instead.

