#demo
[Mirror Lake](http://blog.jswh.me/)
# setup
## dependences
1. git
2. python3
3. virtualenv

## steps
1. fork this repo, change the repo name to `$your_user_name.github.io`
2. in terminal, get into the repo directory and run `./setup`. windows users may follow the steps in file `setup`
3. change pelicanconf.py to your own blog information
4. set your own domain in `CNAME`(optional)
5. run `./publish`, done

# usage
## add content
Add content like `content.md` to `content` directory and execute `./publish`.

## pelican
The blog generator is [pelican](http://docs.getpelican.com/en/3.6.3/quickstart.html#create-an-article).
You can change every thing as long as pelican support.The default theme is [Flex](https://github.com/alexandrevicenzi/Flex/tree/5bc235cf579cb03bcc8f54b6029ff74493a0cb44).
