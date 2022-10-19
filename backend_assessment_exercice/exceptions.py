from rest_framework import exceptions, status


class ServiceUnavailableError(exceptions.APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = "Service unavailable."
