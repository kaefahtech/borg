class TestDockerManager:
	def test_can_instantiate_docker_manager_class(self):
		""" Test DockerManager class """
		from app.docker_manager import DockerManager
		docker_manager = DockerManager()
		assert isinstance(docker_manager, DockerManager)
