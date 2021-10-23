from botocore.stub import Stubber

from comprehend_client import ComprehendClient, ComprehendResponse, S3Client


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
       # assert actual == ComprehendResponse.parse_obj(response)


def test_s3_client():

    client = S3Client()

    actual = client.get_object(bucket_name="c2chackathon", key="professionaltraining.cvs")
    #assert actual == ""

def test_professionalist():
    response = {
        

        "Classes": [
        {
            "Name": "PROFESSIONAL",
            "Score": 0.9946833252906799
        },
        {
            "Name": "UNPROFESSIONAL",
            "Score": 0.005316717550158501
        }
        ]
    }

    classes = response["Classes"]
    for clazz in classes:
        if clazz["Name"] == "PROFESSIONAL" and clazz["Score"] >= 0.65:
            print(f"Your Professionalism score is: {clazz['Score']*100} ! This means that your resume is on the right track!")
        else:
            print(f"Your Professionalism score is:  {clazz['Score']*100}! To improve your score check out our resources on our Resources tab!")
            
            
        