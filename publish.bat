set CDIR=%~dp0
call %CDIR%\Scripts\activate.bat
git add .
git commit -a -m "write article"
git push origin pelican
cp %CDIR%\CNAME %CDIR%\output\CNAME
ghp-import -m "Generate Pelican site" -b master %CDIR%\output
git push origin master
pause