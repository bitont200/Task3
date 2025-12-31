import docker

client = docker.from_env()

container = client.containers.run(
    image="busybox",
    command=["sleep", "1000"],
    detach=True
)

result = container.exec_run("hostname")

print("Container hostname:", result.output.decode().strip())

container.stop()
container.remove()
