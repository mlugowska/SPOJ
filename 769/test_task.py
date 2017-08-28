from builtins import input


def test_task():
    a = int(input())
    assert (a < 200), 'Enter value less than 200'

    b = int(input())
    assert (b < 200), 'Enter value less than 200'
    print(a + b)

if __name__ == '__main__':
    test_task()
