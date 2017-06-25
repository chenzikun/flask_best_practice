/**
 * Created by chenzikun on 2017/6/23.
 */
const nunjucks = require('nunjucks');
const express = require('express');
const path = require('path');
var data = require('./data.json');

var app = express();

var base_dir = path.join(__dirname, '../..');
var templates = path.join(base_dir, 'templates');

// templates
env = nunjucks.configure(templates, {
    autoescape: true,
    express: app,
    watch: true,
    noCache: true
});

// 让url_for编译过去
env.addGlobal('url_for', function () {
    return '#';
});

// static files
app.use(express.static(base_dir));

// 模板渲染 index索引页
app.get('/', function (req, res) {
    res.render('index.html', {
        data: data.index
    });
});

// 模板渲染 homepage首页
app.get('/homepage', function (req, res) {
    res.render('homepage.html', {
        data: data.index
    });
});

var thisTemplatePort = 5100;
// 启动服务
app.listen(thisTemplatePort);
console.info('监听成功，请在浏览器访问 http://localhost:', thisTemplatePort);