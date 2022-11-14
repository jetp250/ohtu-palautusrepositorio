from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        as_toml = toml.loads(content)
        poetry_desc = as_toml['tool']['poetry']

        name = poetry_desc['name']
        description = poetry_desc['description']
        dependencies = poetry_desc['dependencies']
        dev_dependencies = poetry_desc['dev-dependencies']

        return Project(name, description, dependencies, dev_dependencies)
