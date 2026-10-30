from abc import ABC
from typing import TypeVar
from flask import g

class Service(ABC):
    """
    Abstract base class for services.
    Expects a service container to be passed during initialization.
    """

    def __init__(self, service_container: ServiceContainer):
        self.service_container = service_container

T = TypeVar('T', bound=Service)

class ServiceContainer:
    """
    Service container class for managing services.
    """

    def __init__(self):
        self.__services = {}

    def _init_service(self, service: type[T]) -> T:
        """
        Initializes a service and stores it in the container.
        """

        init_service = service(self)
        self.__services[service] = init_service
        return self.__services[service]

        
    def get_service(self, service: type[T]) -> T:
        """
        Retrieves a service from the container.
        """

        if service in self.__services:
            return self.__services[service]
        return self._init_service(service)

def get_service_container() -> ServiceContainer:
    """
    Retrieves the service container from the application context.
    """

    if 'service_container' not in g:
            g.service_container = ServiceContainer()

    return g.service_container