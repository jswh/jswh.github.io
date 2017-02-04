set CDIR=%~dp0
set Python=%LOCALAPPDATA%\Programs\Python\Python35-32\python.exe
git clone https://github.com/jswh/Flex.git Flex
pip install virtualenv -i https://pypi.doubanio.com/simple/
virtualenv -p %Python% --no-site-packages %CDIR%
call %CDIR%\Scripts\activate.bat
pip install -i https://pypi.doubanio.com/simple/ pelican markdown ghp-import six
pelican-themes -s %CDIR%\Flex
pause