import os

def create_temp_directory(path, name):
    if not os.path.exists(os.path.join(path, name)):
        os.mkdir(os.path.join(path, name))

if __name__ == "__main__":
    name = 'tmp'
    create_temp_directory('.', name)
    os.chdir(f'./{name}')

    print(os.getcwd())