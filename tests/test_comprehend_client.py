from botocore.stub import Stubber

from comprehend_client import ComprehendClient, ComprehendResponse


def test_comprehend_client():
    response = {
        'Classes': [
            {
                'Name': 'class1',
                'Score': 1.0
            },
            {
                'Name': 'class2',
                'Score': 2.0
            }
        ],
        'Labels': [
            {
                'Name': 'label1',
                'Score': 1.0
            },
            {
                'Name': 'label2',
                'Score': 2.0
            }
        ]
    }

    client = ComprehendClient()
    stubber = Stubber(client.client)
    expected_params = {"Text": "foo", "EndpointArn": "bar"}
    stubber.add_response('classify_document', response, expected_params)

    with stubber:
        actual = client.classify_document(text="foo", endponint_arn="bar")
        assert actual == ComprehendResponse.parse_obj(response)

def test_s3_client():

    client = s3_Client()
    
    actual = client.get_object(Bucket="c2chackathon", key="professionaltraining.cvs")
    print (actual)