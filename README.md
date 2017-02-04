#demo
[Mirror Lake](http://blog.jswh.me/)
# setup
## dependences
1. [git](https://git-scm.com/)
2. [python3](https://www.python.org/downloads/)

## steps
1. fork this repo, change the repo name to `$your_user_name.github.io`
2. in terminal, get into the repo directory and run the setup script. 
    * `setup` for *nix users
    * `setup.bat` for windows users, and "run as administrator" is recommended
3. change options in `pelicanconf.py` to your own blog information
4. set your own domain in `CNAME`(optional)
5. execute the publish script, done
    * `publish` for *nix users
    * `publish.bat` for windows users

# usage
## add content
Add content like `content.md` to `content` directory and execute the publish script.

## pelican
The blog generator is [pelican](http://docs.getpelican.com/en/3.6.3/quickstart.html#create-an-article).
You can change every thing as long as pelican supported.The default theme is [Flex](https://github.com/alexandrevicenzi/Flex/tree/5bc235cf579cb03bcc8f54b6029ff74493a0cb44).`