import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="bbtm-vivekascoder",
    version="0.0.1",
    author="Vivek Kumar",
    author_email="vivekascoder@gmail.com",
    description="A package to export your browser bookmarks.",
    long_description=long_description,
    long_description_content_type="text/marksdown",
    url="https://github.com/vivekascoder/bbtm",
    project_urls={
        "Bug Tracker": "vivekascoder@gmail.com",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix/Linux",
    ],
    packages=setuptools.find_packages(),
    python_requires=">3.0",
)
