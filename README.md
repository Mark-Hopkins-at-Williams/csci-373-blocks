Github Classroom Assignment Template 
-------------------------------------

### Creating a Github Classroom Assignment

1. Once the unittest file ```test.py``` is ready, encrypt it with the command:

       python encrypt.py CRYPTO_KEY test.py

   and then delete ```test.py```.

2. When creating the assignment, make sure to check the box next 
to **Enable feedback pull requests**.

3. To add an autograding test to a Github Classroom Assignment,
- **Setup command** should be:

       sudo -H pip3 install pytest cryptography >/dev/null

- **Run command** should be:

       python3 autograder.py CRYPTO_KEY TEST_CLASS_NAME


### Example Assignment Description for Students

The assignment description can be found here.

This repository contains a starter file for the code you need to write:
- `hw.py`: Put code in this file.

Ignore (but do not delete!!!) the other files in this repository.