import sys
from pathlib import Path
from colorama import Fore, Style, init

def get_tree_visualization(path):
    init(autoreset=True)
    root_directory = Path(path).resolve()
    if not root_directory.exists():
        print(f"Root is not found: {root_directory}")
        return

    def color_name(p: Path) -> str:
        if p.is_dir():
            return Fore.BLUE + p.name + "/" + Style.RESET_ALL
        return Fore.GREEN + p.name + Style.RESET_ALL

    def children(dir_path: Path):
        items = []
        default_ignore = {".git", "__pycache__", ".venv"}
        for p in dir_path.iterdir():
            if p.name in default_ignore:
                continue
            items.append(p)
        return sorted(items, key=lambda x: (x.is_file(), x.name.lower()))

    def walk(dir_path: Path, prefix: str = "", depth: int = 0):
        entries = children(dir_path)
        for idx, entry in enumerate(entries):
            last = idx == len(entries) - 1
            branch = "└── " if last else "├── "
            print(prefix + branch + color_name(entry))

            if entry.is_dir():
                extension = "    " if last else "│   "
                walk(entry, prefix + extension, depth + 1)

    walk(root_directory)

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    get_tree_visualization(path)

