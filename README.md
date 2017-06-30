# Demo

## 技术选型
1. 后台：Flask
2. 前端：nunjucks, bootstrap, gulp
3. 数据库： redis, mysql

## 部署方案

Flask + Gunicorn + Nginx 部署
* 打算改为docker

## 启动
* make up 启动gunicorn伺服

## nginx配置
* config/default


## pip下载源

* 将以下网址放在requirements.txt首句

 > --index https://pypi.douban.com/simple

## redis高可用
* 采用docker容器方案部署redis高可用

## 关于端口
1. docker下，暴露为8000，可将本地映射为8800
2. gulp下访问端口为5100, 并占据5010端口
3. Python下访问端口为8080

## Makefile