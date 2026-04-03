# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "watchfiles>=1.1.1",
# ]
# ///

# import libraries
import atexit
from pathlib import Path

from watchfiles import watch

wowpy_parent_path = Path(__file__).parent
wowtxt_path = wowpy_parent_path / "wow.txt"


# deletes everything written in wow.txt
def exit_handler():
    with open(wowtxt_path, "w") as f:
        f.write("")
        return


def main():

    # registers termination
    atexit.register(exit_handler)

    # kickstarts loop
    if wowtxt_path.exists():
        wowtxt_path.write_text("wow\n")
        print("loop kickstarted")
    else:
        print(f"{wowtxt_path} does not exist")
        return

    # watches for changes in wow_path (wow.txt)
    for changes in watch(wowtxt_path):
        with open(wowtxt_path, "a") as f:
            f.write("wow\n")


if __name__ == "__main__":
    main()

# created by unsandpiper8 1/4/2026 for the python-9246 repo.