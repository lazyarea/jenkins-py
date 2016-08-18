    # jenkins-py

    yum install gcc zlib-devel bzip2 bzip2-devel readline readline-devel sqlite sqlite-devel openssl openssl-devel git
    git clone https://github.com/yyuu/pyenv.git ~/.pyenv

    pyenv install 3.4.1
    pyenv global 3.4.1
    pyenv rehash
    pyenv version

    django-admin startproject mysite
    cd mysite
    ../bin/python manage.py runserver

    pip install -r requirement.txt
