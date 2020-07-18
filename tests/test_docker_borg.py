from app.docker_borg import DockerManager
from app.installer import Installer


class TestDockerManager:
	def test_can_instantiate_docker_manager_class(self):
		""" Test DockerManager class """
		docker_manager = DockerManager()
		assert isinstance(docker_manager, DockerManager)


class TestInstaller:
	def test_can_instantiate_installer_base_class(self):
		""" Test Installer base class """
		Installer.__abstractmethods__ = set()
		installer = Installer()
		assert isinstance(installer, Installer)
		installer.install

# class TestDockerInstaller:
# 	def test_can_instantiate_docker_installer_class(self):
# 		""" Test DockerInstaller class """
# 		from app.docker_borg import DockerInstaller
# 		docker_installer = DockerInstaller()
# 		assert isinstance(docker_installer, DockerInstaller)