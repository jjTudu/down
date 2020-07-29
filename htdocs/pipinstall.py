import sys
import subprocess

class App:
    def __init__(self, virtual_dir):
        self.virtual_dir = virtual_dir
        self.virtual_python = os.path.join(self.virtual_dir, "Scripts", "python.exe")

    def install_virtual_env(self):
        self.pip_install("virtualenv")
        if not os.path.exists(self.virtual_python):
            import subprocess
            subprocess.call([sys.executable, "-m", "virtualenv", self.virtual_dir])
        else:
            print("found virtual python: " + self.virtual_python)

    def is_venv(self):
        return sys.prefix==self.virtual_dir

    def restart_under_venv(self):
        print("Restarting under virtual environment " + self.virtual_dir)
        subprocess.call([self.virtual_python, __file__] + sys.argv[1:])
        exit(0)

    def pip_install(self, package):
        try:
            __import__(package)
        except:
            subprocess.call([sys.executable, "-m", "pip", "install", package, "--upgrade"])

    def run(self):
        if not self.is_venv():
            self.install_virtual_env()
            self.restart_under_venv()
        else:
            print("Running under virtual environment")