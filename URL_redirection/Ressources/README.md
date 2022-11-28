
# How to get the flag

At the bottom of the pages, you can find redirection links to facebook, twitter or instagram :
```
http://192.168.0.10:8080/index.php?page=redirect&site=facebook
```

You can replace the "site" parameter to a malicious site and voila!
```
http://192.168.0.10:8080/index.php?page=redirect&site=mouhahaha.com
```

# How to prevent attack

You can prevent this attack by URL validation and avoiding to put redirection parameters in the URL.

# Documentation


https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html
