# from django.test import TestCase
import os
import os.path
# Create your tests here.
def os_test():
    print(os.getcwd())
    print(os.name)
    # os.chdir("../")
    # print(os.getcwd())
    file_path = os.path.join(os.getcwd(), "course", "tests.py")
    
    if os.path.exists(file_path):
        print(os.stat(file_path))
    else:
        print("File not found")

if __name__ == "__main__":
    os_test()