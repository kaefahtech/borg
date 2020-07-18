""" Installer abstract module """
from abc import ABC, abstractmethod


class Installer(ABC):
	""" Installer interface class to declare install interface """

	@abstractmethod
	def install(self):
		""" Install method to be implemented by installers """
		pass
