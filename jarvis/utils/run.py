import subprocess


class RunFile():

    def __init__(self, **kwargs):
        self.file_name = ""
        self.file_path = ""

    def run(self, path, name):
        """
        Run a file.
        """
        self.file_name = name
        self.file_path = path

        # @TODO: Replace "python" with dynamic language name
        # @TODO: Remove "shell=True" and figure out a way to make it work
        #   with out it
        subprocess.Popen("python " + self.file_path + self.file_name, shell=True)

        # @TODO: Return the program's output
        return
