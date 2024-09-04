# gdl.py
This python script is a workaround for me to download images with ampersands (`&`) in the URL using [gallery-dl](https://github.com/mikf/gallery-dl/).

It does it in a way that doesn't require you to change the URL in the terminal.

There's probably a better way that doesn't require a python script, but I can't find it.

## Setup

- Download [gallery-dl.exe](https://github.com/mikf/gallery-dl/releases/) and place it in any directory you want.
- Download gdl.py and move it to the same folder as `gallery-dl.exe`.
- Download python

I also recommend making a gallery-dl.conf file for sites you might need to sign in to

## Usage

1. Open your terminal in the directory containing `gallery-dl.exe` and `gdl.py`.
2. Run `python gdl.py` and input the URLs to download.

### Example
```
PS D:\gallery-dl> python.exe .\gdl.py
Enter URLs for gallery-dl (type 'quit', 'exit', or '3' to exit)
> https://gelbooru.com/index.php?page=post&s=view&id=6954271 https://gelbooru.com/index.php?page=post&s=view&id=197798
[1/2] https://gelbooru.com/index.php?page=post&s=view&id=6954271
.\gallery-dl\gelbooru\gelbooru_6954271_9ef30a52d3c324640ba63a463e9cc7c4.jpg
[2/2] https://gelbooru.com/index.php?page=post&s=view&id=197798
.\gallery-dl\gelbooru\gelbooru_197798_3c5dd70262f440630adfc1f9bb7d5da1.jpg
Enter URLs for gallery-dl (type 'quit', 'exit', or '3' to exit)
> exit
```
