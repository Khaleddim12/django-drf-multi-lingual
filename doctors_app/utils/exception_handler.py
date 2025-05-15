from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, AuthenticationFailed, NotAuthenticated, PermissionDenied, Throttled
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import Throttled as DjangoThrottled


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Bad request')
    default_code = 'bad_request'
    
class ValidationError(APIException):
    status_code = 400
    default_detail = _('Invalid input.')  # <-- This is where it comes from
    default_code = 'invalid'

class Unauthorized(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Unauthorized')
    default_code = 'unauthorized'


class Forbidden(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = _('Permission denied')
    default_code = 'permission_denied'


class TooManyRequests(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = _('Request was throttled')
    default_code = 'throttled'


class ServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = _('Server error')
    default_code = 'server_error'


class GatewayTimeout(APIException):
    status_code = status.HTTP_504_GATEWAY_TIMEOUT
    default_detail = _('Gateway timeout')
    default_code = 'gateway_timeout'


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

    if isinstance(exc, (ValidationError, BadRequest)) or getattr(exc, 'default_code', None) == 'invalid':
        error_data = {
            'error': str(exc.default_detail) if hasattr(exc, 'default_detail') else _('Bad request'),
            'detail': exc.detail if hasattr(exc, 'detail') else str(exc),
            'code': exc.default_code if hasattr(exc, 'default_code') else 'invalid'
        }
        return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

    elif isinstance(exc, (AuthenticationFailed, NotAuthenticated, Unauthorized)):
        # Handle 401 Unauthorized
        error_data = {
            'error': str(exc.default_detail) if hasattr(exc, 'default_detail') else _('Unauthorized'),
            'detail': exc.detail if hasattr(exc, 'detail') else str(exc),
            'code': exc.default_code if hasattr(exc, 'default_code') else 'unauthorized'
        }
        return Response(error_data, status=status.HTTP_401_UNAUTHORIZED)

    elif isinstance(exc, (PermissionDenied, Forbidden)):
        # Handle 403 Forbidden
        error_data = {
            'error': str(exc.default_detail) if hasattr(exc, 'default_detail') else _('Forbidden'),
            'detail': exc.detail if hasattr(exc, 'detail') else str(exc),
            'code': exc.default_code if hasattr(exc, 'default_code') else 'permission_denied'
        }
        return Response(error_data, status=status.HTTP_403_FORBIDDEN)

    elif isinstance(exc, (Throttled, DjangoThrottled, TooManyRequests)):
        # Handle 429 Too Many Requests
        wait_time = getattr(exc, 'wait', None)
        detail = _('Expected available in %d seconds.') % wait_time if wait_time else _('Too many requests')
        
        error_data = {
            'error': str(exc.default_detail) if hasattr(exc, 'default_detail') else _('Too many requests'),
            'detail': detail,
            'code': exc.default_code if hasattr(exc, 'default_code') else 'throttled'
        }
        return Response(error_data, status=status.HTTP_429_TOO_MANY_REQUESTS)

    elif isinstance(exc, ServerError):
        # Handle 500 Internal Server Error
        error_data = {
            'error': str(exc.default_detail) if hasattr(exc, 'default_detail') else _('Server error'),
            'detail': str(exc),
            'code': exc.default_code if hasattr(exc, 'default_code') else 'server_error'
        }
        return Response(error_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif isinstance(exc, GatewayTimeout):
        # Handle 504 Gateway Timeout
        error_data = {
            'error': str(exc.default_detail) if hasattr(exc, 'default_detail') else _('Gateway timeout'),
            'detail': str(exc),
            'code': exc.default_code if hasattr(exc, 'default_code') else 'gateway_timeout'
        }
        return Response(error_data, status=status.HTTP_504_GATEWAY_TIMEOUT)

    # For unhandled exceptions
    elif response is None:
        error_data = {
            'error': _('Server error'),
            'detail': str(exc),
            'code': 'server_error'
        }
        return Response(error_data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response