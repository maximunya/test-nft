from drf_yasg.openapi import Schema, TYPE_OBJECT, TYPE_STRING, TYPE_INTEGER
from drf_yasg.utils import swagger_auto_schema


def token_create_schema():
    return swagger_auto_schema(
        request_body=Schema(
            type=TYPE_OBJECT,
            properties={
                'media_url': Schema(type=TYPE_STRING, description='Media URL'),
                'owner': Schema(type=TYPE_STRING, description='Owner address'),
            },
            required=['media_url', 'owner']
        ),
        responses={
            201: Schema(
                type=TYPE_OBJECT,
                properties={
                    'id': Schema(type=TYPE_INTEGER, description='Token ID'),
                    'unique_hash': Schema(type=TYPE_STRING, description='Unique hash'),
                    'media_url': Schema(type=TYPE_STRING, description='Media URL'),
                    'owner': Schema(type=TYPE_STRING, description='Owner address'),
                    'tx_hash': Schema(type=TYPE_STRING, description='Transaction hash'),
                }
            )
        }
    )

def total_supply_schema():
    return swagger_auto_schema(
        responses={
            200: Schema(
                type=TYPE_OBJECT,
                properties={
                    'result': Schema(type=TYPE_INTEGER, description='Total amount of tokens')
                }
            )
        }
    )