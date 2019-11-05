const express = require("express")
const serveStatic = require("serve-static")
const path = require('path')
const proxy = require('express-http-proxy'); 
const history = require('connect-history-api-fallback');

const app = express()

//add this middleware
app.use(history());  

app.use('/api', proxy('https://krist-9323-backend.herokuapp.com'))
app.use('/', serveStatic(path.join(__dirname, '/dist')))

const port = process.env.PORT || 8080
app.listen(port)

console.log("Server is running on port " + port)
