"""Fetch Micropython packages and put them on packages folder."""
import io
import sys
import os
import requests
import tarfile


def main():
    """Run main function."""
    arguments = sys.argv[1:]

    if len(arguments) != 1:
        raise Exception("It must be provided a path to requirements file.")

    requirements_file = arguments[0]
    if not os.path.isfile(requirements_file):
        raise Exception("Requirements file is not a file.")

    with open(requirements_file, "r") as file:
        requirements = file.readlines()

    for req in requirements:
        print("Fetching package:", req)
        req = req.strip()
        r = requests.get(req)
        if r.status_code != 200:
            raise Exception("Requirement not found:", req)

        content_type = r.headers["Content-Type"]
        if 'application/x-gzip' == content_type:
            content_io = io.BytesIO(r.content)
            content_io.seek(0)

            with tarfile.open(fileobj=content_io, mode='r:*') as tar_data:
                members = tar_data.getmembers()
                list_members = []
                for m in members:
                    splited = m.name.split("src/")
                    if 2 == len(splited):
                        temp_m = m.replace(name=splited[1])
                        list_members.append(temp_m)
                tar_data.extractall(
                    path="lib", members=list_members)


if __name__ == "__main__":
    main()
