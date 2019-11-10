import logging
import os
import boto3
from botocore.exceptions import ClientError
from random import randrange

def create_presigned_url(object_name):
    """Generate a presigned URL to share an S3 object with a capped expiration of 60 seconds

    :param object_name: string
    :return: Presigned URL as string. If error, returns None.
    """
    s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=60*1)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response

def get_all_songs():
    s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4',s3={'addressing_style': 'path'}))
    try:
        bucket_name = os.environ.get('S3_PERSISTENCE_BUCKET')
        response = s3_client.list_objects_v2(Bucket = bucket_name)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response['Contents']

def get_random_song():
    all_songs = get_all_songs()
    random_song_index = randrange(len(all_songs)-1)
    return all_songs[random_song_index]['Key']