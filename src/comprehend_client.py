import logging
from typing import Optional, List

import boto3
from boto3_type_annotations.comprehend import Client
from pydantic import BaseModel


class Classes(BaseModel):
    Name: str
    Score: float


class Labels(BaseModel):
    Name: str
    Score: float


class ComprehendResponse(BaseModel):
    Classes: List[Classes]
    Labels: List[Labels]


class ComprehendClient:
    def __init__(self, region_name: str = "us-west-2"):
        self.client: Optional[Client] = None
        self.region_name = region_name
        self.logger = logging.getLogger(__name__)

    @property
    def client(self) -> Client:
        if self.__client is None:
            self.__client = boto3.client("comprehend", region_name=self.region_name)
        return self.__client

    @client.setter
    def client(self, value: Client):
        self.__client = value

    def classify_document(self, text: str, endponint_arn: str) -> ComprehendResponse:
        response = self.client.classify_document(Text=text, EndpointArn=endponint_arn)
        return ComprehendResponse.parse_obj(response)

class s3Client:
    def __init__(self, region_name: str = "us-west-2"):
        self.client: Optional[Client] = None
        self.region_name = region_name
        self.logger = logging.getLogger(__name__)

    @property
    def client(self) -> Client:
        if self.__client is None:
            self.__client = boto3.client("comprehend", region_name=self.region_name)
        return self.__client

    @client.setter
    def client(self, value: Client):
        self.__client = value

    def get_object(self, bucket_name, key):
        response = self.client.get_object(Bucket=bucket_name, Key=key)
        return response

