# How to get the flag
Searching the website with an external app like OWASP Zed Attack Proxy or Burp Suite reveals every existing url of the website.

This particular folder can also be found looking at the robots.txt file of the website.
The robots.txt file tells the search engine what url you don't want to appear when searching for your website.
This gives us a hint as to what url contains vulnerable information.
And even though these disallowed urls won't appear on a search engine, you can still browse them so doing this does not secure these urls.

With this, we found the existence of a .hidden folder with autoindex activated.
This means that when exploring this url, every single folder and file in this folder is navigable.

Of course, just giving us the flag right away would be too easy ; there are thousands of folders in there, each nested in one another. And only one of these folders contain the flag so brute forcing it won't cut it.

I needed to write a script which would recursively download every single README in every single folder, put them all in one file and then sort that file to look for the flag.

Running the script.sh (while making sure the correct address is in the script) does exactly that.
There are over 17 000 READMEs in there so the script takes a while to finish computing.

# How to prevent attack
Putting an url in robots.txt file does not prevent it from being navigable
Setting autoindex off.
Making sure the folders containing sensitive information are forbidden from access.
