# Python Flask Hello World

[![CI to Docker Hub](https://github.com/arska/postgres-helloworld/actions/workflows/docker-image.yml/badge.svg)](https://github.com/arska/postgres-helloworld/actions/workflows/docker-image.yml)

This is a very lightweight demo web application serving the Postgresql "PING" on TCP port 8080

I use it to demo application deployment to OpenShift on https://appuio.ch

- Web-GUI: "Add to project" -> search for "Python" -> Choose "Python" -> Next -> Version: 3.9 Name: postgres-helloworld, Git Repository: https://github.com/arska/postgres-helloworld.git -> Create -> Close

- CLI using source-to-image (s2i)

```
oc new-app python:3.9~https://github.com/arska/postgres-helloworld.git; oc expose service postgres-helloworld
```

- CLI using Dockerfile

```
oc new-app --strategy=docker https://github.com/arska/postgres-helloworld.git; oc expose service postgres-helloworld
```

You can clean up after with:

```
oc delete all -l app=postgres-helloworld
```

You can also build and run this locally using docker

```
docker build -t postgres-helloworld .
docker run -p 8080:8080 postgres-helloworld
```

the application is then accessible at http://127.0.0.1:8080/
