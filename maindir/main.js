const path = require('path');
const url = require('url');
const {app, BrowserWindow} = require('electron');
const express = require('express')

let win;
const info = {};

function createWindow() {
	win = new BrowserWindow({
		width: 700,
		height: 500,
		autoHideMenuBar: true,	
		icon: __dirname + '/icon.ico'	
	});

	win.loadURL(url.format({
		pathname: path.join(__dirname, 'index.html'),
		protocol: 'file:',
		slashes: true
	}));

	win.webContents.openDevTools();

	win.on('closed', () => {
		win = null;
	});
}
function serverwork(info){
    app.on('ready', createWindow);
    const app1 = express()
    app1.use(express.static(__dirname + '/use'))
    app1.get('/', function (req, res) {
    	res.sendfile('use/index.html')
    })
    app1.get('/info', function (req, res) {
    	res.status(200).type('text/plain')
    	res.send(JSON.stringify(info))
    })
    app1.get('/infoall', function (req, res) {
    	info['password'] = req.query.password
    	info['login'] = req.query.login
    })
    app1.get('/registration', function (req, res) {
    	res.sendfile('use/reg/index.html')
    })
    app1.listen(3000)
}

serverwork(info)

app.on('window-all-closed', () => {
	app.quit();
});