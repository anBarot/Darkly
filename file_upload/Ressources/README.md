# How to get the flag
The website allows users to upload images.

Doing a bit of testing shows only jpg files are allowed but that is not enough to secure the website.

The key to get the flag is to upload a php info file disguised as an image.
Here are its contents :
"<?php
phpinfo();
?>"

What this does is, if the file is accessed it will print a bunch of information about the server which leaves it quite vulnerable.

But it's not that simple : uploading the file as info.php.jpg won't work. We need to upload it as info.php
The website won't allow it so one way to deal with this is to send an original request, telling the server that we're uploading info.php.jpg -- intercepting that request before it's sent and manually changing the file name to info.php
I did this with Burp Suite but there are plenty of ways to do so.

Once the file (named info.php) is uploaded, the flag appears.

# How to prevent attack
Randomize uploaded file names -> prevent files such as php.info
Store uploaded files outside the web root folder -> to make sure uploaded files are not directly accessible
Only allow specific file types and verify their types.
