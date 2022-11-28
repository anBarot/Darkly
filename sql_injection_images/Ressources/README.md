# How to get the flag
It is possible to inject the website with SQL on the searchimg page.

In the input field, you can write SQL commands which will be read and processed by SQL.
The returned values of the SQL command need to be able to fit in the original spreadsheet.
If the spreadsheet contains two columns, then that is the space we have to fit anything we'd like to print.

For example, if I write in the input field "1 OR 1=1" :
	- the first "1" is simply the ID of the member I'm looking for
	- "OR 1=1" tells SQL that we also want any ID in the database (because 1=1 is a true proposition, so every ID falls into that category)

Doing this shows us a list of the images on the site and we can see one is named "Hack me ?".
Now we can try to get more information about this img.

To know what information is available, you could write in the input field
"1 UNION SELECT table_name, column_name FROM information_schema.columns"
Now, we have a list of every single table and their columns.
Looking at the list_images table, we can see there are many more columns than those that are printed on the spreadsheet.
So let's print them!

"1 UNION SELECT id, CONCAT(url, title, comment) FROM list_images"

The reason we're concatenating every column into one is because we only have space for two columns, so this is the way to read more information without having to do repeat queries.

Though actually, only the comment column is required to get the flag.

Here's the output:
"borntosec.ddns.net/images.pngHack me ?If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46"

# How to prevent attack

Using prepared statements.
Form validation, sanitize input.

