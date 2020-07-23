# flask的web服务
======================

:Date: 2020-07-23


环境搭建
-----------

.. code:: bash
    
    sudo apt-get install python3.6
    sudo apt-get install python3-pip

    sudo pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

    cd flask_basic_template
    python3 manage.py init

运行
--------------------

.. code:: bash
    
    cd flask_basic_template
    python3 manage.py runserver
    # Or run in shell
    cd flask_basic_template
    python3 manage.py shell


补充部分
------------------
* 短信验证码
