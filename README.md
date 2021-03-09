项目后端用flask，前端用vue，做一个移动端的健康咨询app。

Vue版本为Vue2.x

## 运行app

1. 下载此项目。

2. 命令行中打开项目的`back_end`文件夹，安装`requirements.txt`文件中的第三方包，运行`app.py`文件。

   ```sh
   $ cd back_end
   $ python3.9 -m venv env
   (env)$ pip install -r requirements.txt
   (env)$ python app.py
   ```

   后端接口为： http://localhost:8080

   提示：需将`app.py`文件中的`localhost`地址改为本地的`IPv4`地址。

3. 在另外一个命令行中打开`front_end`文件夹，安装第三方包，并运行。

   ```sh
   $ cd front_end
   $ npm install
   $ npm run serve
   ```

   前端网址为： http://localhost:8999

   提示：需将`vue.config.js`和`src/assets/js/globalConfig.js`文件中的`localhost`地址改为本地的`IPv4`地址。