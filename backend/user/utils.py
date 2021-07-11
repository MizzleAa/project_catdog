from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if 'detail' in response.data:
        error_message = response.data['detail']
        response.data = {
            'error': error_message
        }

    return response
