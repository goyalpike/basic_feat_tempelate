# Notes are based on the [Complete Docker Course](https://www.youtube.com/watch?v=RqTEHSBrYFw&t=13148s)

## What is a container?
- A docker container image is a lightwrights, standalong, executable package of software that includes everything needed to run an application. 

## Difference between VM and containers?
- VMs have their own copy of linux kernel, or in general operating system kernel, whereas containers shares kernel with the host operating system. However, containers have specific faetures that enable to have isolation enviornment quite good.  
- Containers have a weaker isolation that VMs with other advantanges such as having their own binaries and libraries. 
- Most of cloud applications have several VMs, and containers are run on those VMs.
- *Advantages of Containers*:
  - Faster startup time.
  - Lower resource consumption, thus perfect for development.
  - Flexibility to run different application environments.


## Sharing folders with host and containers
- By deault, all the data created or modified in a containers are ephemeral.
- If we like to have stored these data outside the containers (e.g., when data are generated in run-time of the container), docker provides two options:
  - Volume mount: A designated place in the host is mapped to a path in the container, e.g., `/usr/lib/docker/volumes`.
  - Bind mount: We connect host file path to a path in docker. 
Volume mount is a preferred way as it is much faster if we need to many times read and write. However, we want to check how the data is being stored and how they look like, then we can go for bind mount for development phase.

## What is dockerfile
- A text document that contains all the commands a user could call on the commad line to assemble an image

## Connecting with Jupyter notebook and open in the host machine
- First, make sure that jupyter-lab is installed.
- Make sure than port is set while creating docker container, i.e, `docker run -it --name container_name --rm -p 8888:8888 image_name`
- Then, launch jupyter-lab, i.e., `poetry run jupyter-lab --port=8888 --no-browser --allow-root --ip=0.0.0.0`. Ensure to set ip as well, as suggested else port will not be heard.
- Finally, open `http://localhost:8888/lab`. Hope it goes smoothly. 

## What is container registry?
- A repository, or collection of repositoriesused to store and access container images. 

## Some useful command
- `docker ps`": running docker images. With `-a` flag, we would be able to see all the images including those are not running.
- `docker start my_ubuntu`: to start a container.
- `docker attach my_ubuntu`: to attach the container with the current terminal/shell.
- `docker run --interactive --tty --name my_ubuntu ubuntu:22.04`: running ubuntu image interactively. It will create a container with name `my_ubuntu`.
- `docker run --interactively --tty --rm ubuntu:22.04`: running ubuntu image interactively. It will be destroyed once the terminal is exited. 
- `docker volume create my-volume`: Create a volume named `my-volume` which is generally used to store data created in container. Where does this `my-volume` live, please see the discussion [here](https://github.com/sidpalas/devops-directive-docker-course/tree/main/04-using-3rd-party-containers).
- `docker run -it --rm --mount source=my-volume,destination=/my-data/ ubuntu:22.04`:  builds an image that connects my-volume in the host image to my-data in the container. Note that the my-volume folder will be located in the file system in which docker-desktop is built. It is tricky for macos ;-) Check the link given [here](https://github.com/sidpalas/devops-directive-docker-course/tree/main/04-using-3rd-party-containers). We can also include a flag called `--mount type=bind,..` to mount a folder directly in our OS. However, it comes to performace cost. By default, the type is `volume`.
- `docker build -t image_name:tag .` building an image using `Dockerfile` with `image_name` and `tag`.


# Some tips
- `README.md` was important to add if package is installed using poetry. Otherwise poetry will be recognize the folder as package, hence the package will not installed. 