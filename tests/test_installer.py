""" Test cases for installer.py module """
from app.installer import Installer


class TestInstaller:
	def test_can_instantiate_installer_base_class(self):
		""" Test Installer base class """
		Installer.__abstractmethods__ = set()
		installer = Installer()
		assert isinstance(installer, Installer)
		installer.install
