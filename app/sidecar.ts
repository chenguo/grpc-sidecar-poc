import { client } from './proto-shim';

export async function sidecarSum(x: number, y: number) {
  const input = { values: [x, y] };

  return new Promise((resolve, reject) => {
    client.SumInput(input, (error: any, result: any) => {
        if (error) {
          reject(error);
        } else {
          resolve(result);
        }
      });
  });
}

export async function sidecarSumNested(x: number, y: number) {
  const input = {
    input: [{
      value: x,
      label: 'x',
    }, {
      value: y,
      label: 'y',
    }]
  };

  return new Promise((resolve, reject) => {
    client.SumInputNested(input, (error: any, result: any) => {
        if (error) {
          reject(error);
        } else {
          resolve(result);
        }
      });
  });
}
