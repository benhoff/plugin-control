class Plugin:
    def __init__(self, name, src_url=None, pypi_name=None):
        self.name = name
        self.src_url = src_url
        self.pypi_name = pypi_name

plugins = (
        Plugin('pip-plugin', 'https://github.com/benhoff/pip-plugin.git'),
        Plugin('pypi-parser', 'https://github.com/benhoff/pypi-parser.git'),
        Plugin('github-parser', 'https://github.com/benhoff/github-parser.git'),
        )
