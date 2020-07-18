from app.docker_borg import DockerManager


class TestDockerManager:
	def test_can_instantiate_docker_manager_class(self):
		""" Test DockerManager class """
		docker_manager = DockerManager()
		assert isinstance(docker_manager, DockerManager)


class TestDockerInstaller:
	def test_can_instantiate_docker_installer_class(self):
		""" Test DockerInstaller class """
		from app.docker_borg import DockerInstaller
		docker_installer = DockerInstaller()
		assert isinstance(docker_installer, DockerInstaller)

# TODO: Test that we can remove old docker versions from the system
# TODO: Test that we can update the system
# TODO: Test that we can install required packages to allow repo use over HTTPS on system
# TODO: Test that we can add the required GPG key to the system
# TODO: Test that we can verify the fingerprint of the installation on the system
# TODO: Test that we can set up a stable repository with nightly and test repositories
# TODO: Test that we can install a specified version or the latest docker engine on the system
# TODO: Test that we can upgrade a Docker Engine on a system
# TODO: Test that we can set Docker up to be managed by non-root user on a system
# TODO: Test that we can configure Docker to start on boot on a system
# TODO: Test that we can use a different storage engine
# TODO: Test that we can configure a default logging driver on a system
# TODO: Test that we can configure where the Docker daemon listens for connections on a system
# TODO: Test that we can troubleshoot kernel compatibility issues
# TODO: Test that we can resolve IP forwarding problems
# TODO: Test that we can specify DNS servers for Docker
# TODO: Test that we can allow access to the remote API through a firewall
#


