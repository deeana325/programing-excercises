
operators = list('+-*/')

def prepare_input(expr):
    input = expr.split()
    for i in range(len(input)):
        if input[i] not in operators:
            input[i] = int(input[i])
    return input

def calcul(operator, primul_nr, al_doilea_nr):
    if operator == '+':
        return primul_nr + al_doilea_nr
    elif operator == '-':
        return  primul_nr - al_doilea_nr
    elif operator == '*':
        return primul_nr * al_doilea_nr
    elif operator == '/':
        return primul_nr / al_doilea_nr
    else:
        raise Exception(f'invalid operator: {operator}')


def parse_d(input, operator=0, al_doilea_nr=-1):
    if len(input[operator:al_doilea_nr]) == 2:
        return calcul(input[operator], input[al_doilea_nr - 1], input[al_doilea_nr])
    else:
        return calcul(input[operator], parse_d(input, operator + 1, al_doilea_nr - 1), input[al_doilea_nr]) 

print(parse_d(prepare_input('* + 1 2 3')))


# def parse(input):
#     if len(input) == 0:
#         raise Exception('Empty input.')
#     elif input[0] in operators:
#         op = input[0]
#         input_ = input[1:]
#         val1, input_ = parse(input_)
#         val2, input_ = parse(input_)
#         rez = calcul(op, val1, val2)
#         return rez, input_
#     else:
#         return input[0], input[1:]

# def test(expr):
#     rez, input = parse(prepare_input(expr))
#     print(expr, ' -> ',  rez)
#     if len(input) != 0:
#         raise Exception('Too many input symbols')

# test('* - 1 2 3')
