from setuptools import setup, find_packages

setup(
    name="GitHubIssueExtractor",
    version="1.0.0",
    description="GitHubIssueExtractor",
    packages=find_packages(),
    install_requires=[
        "certifi==2022.12.7",
        "charset-normalizer==3.1.0",
        "et-xmlfile==1.1.0",
        "idna==3.4",
        "openpyxl==3.1.2",
        "requests==2.28.2",
        "urllib3==1.26.15",
        "twine==4.0.2"
    ],
    classifiers=[
        "Development Status :: Production",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
