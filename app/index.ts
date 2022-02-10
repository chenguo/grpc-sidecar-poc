import express from 'express';
import { sidecarSum, sidecarSumNested } from './sidecar';

const app = express();

const DefaultPort = 9125;

function getPort(): number {
  const port = parseInt(process.env.PORT ?? '');

  if (isNaN(port)) {
    return DefaultPort;
  } else {
    return port;
  }
}

app.get('/sum', async (req, res) => {
  console.log('sum req.params', req.query);
  try {
    const resp = await sidecarSum(
      req.query.x as unknown as number,
      req.query.y as unknown as number,
    );
    res.send(resp.toObject());
  } catch (error) {
    console.log('error', error);
  }
});

app.get('/sum-nested', async (req, res) => {
  console.log('sum-nested req.params', req.query);
  try {
    const resp = await sidecarSumNested(
      req.query.x as unknown as number,
      req.query.y as unknown as number,
    );
    res.send(resp.toObject());
  } catch (error) {
    console.log('error', error);
  }
});

const port = getPort();
app.listen(port, () => {
  console.log('Node server listening on port', port);
});
