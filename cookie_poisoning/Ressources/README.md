
# How to get the flag

You can find a cookie stored localy :
```
I_am_admin = 68934a3e9455fa72420237eb05902327
```
Decoding in md5 you get the value "false", changing the value by true in md5 :
```
I_am_admin = b326b5062b2f0e69046810717534cb09
``` 
You get the flag !

# How to prevent attack

Critical informations should not be stored in cookies, for example you can store the information in a database 
only accessible through secured requests.

# Documentation

https://www.venafi.com/blog/what-are-cookie-poisoning-attacks-0