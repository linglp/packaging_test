import setuptools
def local_scheme(version):
    return ""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


scm_version_options = {'write_to' : 'src/version.py'}
setuptools.setup(
    name="example-package-linglp",
    use_scm_version={"local_scheme": local_scheme},
    #use_scm_version={'write_to': 'src/version.py'},
    # use_scm_version=True,
    setup_requires=['setuptools_scm'],
    #version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
