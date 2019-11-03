const express = require("express")
const serveStatic = require("serve-static")
const path = require('path')
// const proxy = require('express-http-proxy'); 
const history = require('connect-history-api-fallback');

//add this middleware
app.use(history());  
const app = express()
// app.use('/api', proxy('https://krist-9900-backend.herokuapp.com'))
app.use('/', serveStatic(path.join(__dirname, '/dist')))

const port = process.env.PORT || 8080
app.listen(port)

console.log("Server is running on port " + port)
