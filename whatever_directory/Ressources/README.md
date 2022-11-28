
# How to get the flag

You have a file called robots.txt that you can access. It shows paths that are disallowed for crawler :
- /whatever
- /.hidden

In the file on the path /whatever you have :
```
root:437394baff5aa33daa618be47b75cb49
```
You can decode in md5, you get the admin password. 
In the /admin path you can enter the login credentials and you get the flag.


# How to prevent attack

You can secure the paths access and be vigilant on the information you make accessible.


# Documentation

https://developers.google.com/search/docs/crawling-indexing/robots/intro