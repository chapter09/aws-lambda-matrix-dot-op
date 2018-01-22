import numpy
import boto3
import botocore
import os

BUCKET_NAME = 'aws-lambda-tensorflow' # replace with your bucket name
KEY = os.environ['S3_KEY'] # replace with your object key


def read(fd):
    lines = fd.splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(list(map(int, line.split("\t"))))
        else:
            matrix = B
    return A, B


def printMatrix(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        print("\t".join(map(str,line)))

        
def test_numpy(event, context):
    s3 = boto3.resource('s3')

    try:
        s3 = boto3.client('s3')
        data = s3.get_object(Bucket=BUCKET_NAME, Key=KEY)
        matrix_data = data['Body'].read().decode('utf-8')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise 
    A, B = read(matrix_data)
    A = numpy.matrix(A).T
    B = numpy.matrix(B)
    C = A * B
    return len(C)

