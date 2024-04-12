import tomllib

with open("./pyproject.toml") as f:
    data = tomllib.loads(f.read())

__version__ = data["tool"]["poetry"]["version"]
__version_info__ = tuple(
    [
        int(num) if num.isdigit() else num
        for num in __version__.replace("-", ".", 1).split(".")
    ]
)
