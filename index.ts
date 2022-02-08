import * as express from 'express';

const app = express();


const DefaultPort = 9125;

function getPort(): number {
  const port = parseInt(process.env.PORT);

  if (isNaN(port)) {
    return DefaultPort;
  } else {
    return port;
  }
}

app.get('/call-py', (req, res) => {
  res.send({
    ok: true
  })
});

const port = getPort();
app.listen(port, () => {
  console.log('Node server listening on port', port);
});
