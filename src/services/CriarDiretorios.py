import os


def make():
    os.makedirs('downloads', exist_ok=True)
    os.makedirs('extracted', exist_ok=True)


if __name__ == '__main__':
    make()
