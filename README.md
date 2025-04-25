# NWGen
- Have you ever wonder why would you have to write html everytime?
- Why can't I just write markdown for the website?
<hr></hr>

NWGen is a static website generator from markdown, all you need to do is some .md files and then it will automatically generate html files for you!

## How to run this project
1. Clone this project
2. Put some markdown files into content folder
3. ```./main.sh```
4. Now access localhost:8888 and enjoy (you can change the address to anything you want!)
- **Bonus**: all static files will be in **public** folder, you can change styles and add pictures in **static** folder

## Troubleshoot:
- Python3 is not installed - Install python 3.0+, make sure to remove BOM in main.sh file
- Getting ValueError: No title - The first header (header 1) is the title of the page, if you already have it make sure to remove BOM in all markdown files.
