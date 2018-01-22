import numpy
import json
import os


def parse_matrix(matrix_str):
    lines = matrix_str.splitlines()
    matrix = []
    for line in lines:
        matrix.append(list(map(float, line.split("\t"))))
    return matrix


def render_matrix(matrix):
    matrix = numpy.array(matrix)
    for line in matrix:
        return "\t".join(map(str, line))


def dot_op(A, B):
    A = numpy.matrix(parse_matrix(A))
    B = numpy.matrix(parse_matrix(B))
    return A * B

        
def dot_op_handler(event, context):
    C = dot_op(event['A'], event['B'])
    return json.dumps(C.tolist())


# def test_dot_op_handler():
#     event = {"A": "1\t2\t3", "B": "1\t2\t3"}
#     return dot_op_handler(event, None)
    
    
# if __name__ == '__main__':
#     print(json.loads(test_dot_op_handler())[0])