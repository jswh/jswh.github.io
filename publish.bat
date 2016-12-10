set CDIR=%~dp0
call %CDIR%\Scripts\activate.bat

set INPUTDIR=%CDIR%\content
set OUTPUTDIR=%CDIR%\output
set CONFFILE=%CDIR%\pelicanconf.py
set PUBLISHCONF=%CDIR%\publishconf.py

pelican %INPUTDIR% -o %OUTPUTDIR% -s %PUBLISHCONF% %PELICANOPTS%
git add .
git commit -a -m "write article"
git push origin pelican
cp %CDIR%\CNAME %CDIR%\output\CNAME
python %CDIR%\ghp-win.py -m "Generate Pelican site" -b master %OUTPUTDIR%
git push origin master
pause