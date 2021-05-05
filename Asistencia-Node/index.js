const express = require('express')
const app = express()

var imageToBase64 = require('image-to-base64')

app.get('/', function (req, res) {
  res.sendFile(__dirname + '/index.html');
})

app.listen(3000)
