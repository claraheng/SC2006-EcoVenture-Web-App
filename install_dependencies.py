import subprocess
import sys

# Specify the location of the requirements file
REQUIREMENTS_FILE = 'requirements.txt'

# Define a function to run pip install
def install_dependencies():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', REQUIREMENTS_FILE, '--upgrade'])

# Call the install_dependencies function to install the dependencies
if __name__ == '__main__':
    install_dependencies()
