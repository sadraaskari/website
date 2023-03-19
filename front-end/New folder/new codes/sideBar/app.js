const http = require('http');
const fs = require('fs');
const port = 3000;
const server = http.createServer(function(req , res){
res.writeHead(200 , {'Content-Type' : 'text/html'});
/*const html = fs.readFileSync('./index.html');*/
fs.readFile('test.html' , function(error , data){
    if(error){
        res.writeHead(404);
    }else{
         res.writeHead(data);
    }
    res.end();
});
/*res.end(html);*/
})
server.listen(port , function(error){
    if(error){
        console.log('something went wrong'  , error);
    }else{
         console.log('server is listening port!!!');
    }
});