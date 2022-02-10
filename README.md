# GRPC Sidecar POC

This project is meant to prove out a Typescript server invoking non-Typescript logic on a sidecar container.

The dev environment consists of a docker-compose with a Typescript HTTP server and a Python GRPC server. In a production kubernetes environment this would be two containers running on the same pod.

## Quickstart

Make sure you have docker-compose installed. Then you can run the following commands to bring up the docker-compose environment:

```
$ npm run build
$ npm run up
```

From here you can query the Typescript HTTP server with some calls:

```
$ ./scripts/call-sum.sh 50 100          # basic add numbers endpoint
$ ./scripts/call-sum-nested.sh 5 13     # same, but using messages with nested data
```

## Development

For developing, you may want to run locally instead of inside a docker-compose.

### Python GRPC Sidecar

From the `py-sidecar/` folder, you can bring up the GRPC service by running:

```
$ pip install -r requirements.txt
$ ../scripts/gen-py-pb.sh
$ python app/app.py
```

The code generation script will load `add-things.proto` and generate `app/add_things_pb2.py` and `app/add_things_grpc_pb2.py`, which are needed for starting the GRPC server. You can run example queries against this server:

```
$ python app/call_sum.py
$ python app/call_sum_nested.py
```

### Typescript HTTP Server

From the top level of the repo, you can bring up the HTTP server by running:

```
$ npm ci
$ ./scripts/gen-ts-pb.sh
$ ts-node app/index.ts
```

The code generation script will load `add-things.proto` and generate `app/gen/add_things.ts`, which is needed for starting the server. You can run example queries against this server with the same scripts used in the [Quickstart](#quickstart) section, but do note you'll need to have the Python GRPC server also running to receive any successful responses.


## Notes on Generated Code

**Avoid checking in generated code**

Always have the CI/CD process generate code for testing / deploying. If you rely on manually checking in generated code when you change the underlying `.proto` file, it's too easy to forget and end up not having your new changes deployed.

**Dynamic vs static Node GRPC**

Node's Protobuf implementation has the ability to dynamically load a `.proto` file and generate Javascript objects from it, at run time. For Typescript, this is not desirable, as it's impossible for the Typescript engine to know anything about the interface of the generated objects. For this POC project, we opt to generate a static `.ts` file from the `.proto` definition and work with the explicit interface that provides.
