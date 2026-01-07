from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from continuing_education.domain.exceptions.domain_exception import DomainException

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # If the exception is a DomainException (our custom exceptions)
    if isinstance(exc, DomainException):
        data = {
            "error": exc.message,
            "message": "Validation Error"
        }
        # Use the status code defined in the exception class, or default to 400
        status_code = getattr(exc, 'status_code', status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status_code)

    # If response is None, it might be a generic 500 error or something DRF didn't catch provided it's configured to handle it
    # However, for DRF ValidationErrors (which return a response), we can customize them too if we want
    if response is not None:
        # Standardize DRF ValidationError format
        if response.status_code == 400 and isinstance(response.data, (dict, list)):
             # Flatten errors for simplicity or keep structure but wrap it
             return Response({
                 "error": response.data,
                 "message": "Validation Error"
             }, status=status.HTTP_400_BAD_REQUEST)

    return response
