What is Colima? <br>
Colima is a Linux VM in which we can run Docker and K3s. This will act as the Docker Daemon that normally comes with Docker Desktop.


<br>Installing Docker-cli <br>
Now install the Docker-cli and docker-compose without the docker desktop
``` 
brew install docker docker-compose
```



Installation of Colima <br>
Colima is available on Homebrew and can be installed using the command below.<br> 
```
brew install colima
```


Setting up the Colima VM for Docker<br>
The Colima VM will connect to docker which allows us to use the docker-cli like we are used to.<br>
Running the following command will start the VM.<br>
```
colima start
```

Create Symlinks for Docker Compose (if necessary) <br>
Sometimes, you might need to create symlinks to ensure Docker Compose works correctly with Colima. <br>
```
mkdir -p ~/.docker/cli-plugins
ln -sfn $(brew --prefix)/opt/docker-compose/bin/docker-compose ~/.docker/cli-plugins/docker-compose
```

Helpfull links<br>

- https://github.com/abiosoft/colima
- https://github.com/abiosoft/colima#customizing-the-vm


