import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
version = "0.0.0"

REPO_NAME = "SummarAIze"
AUTHOR_USER_NAME = "dhimanshashank"
SRC_REPO = "SummarAIze"
AUTHOR_EMAIL = "dhimanshashank15@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="SummarAIze: AI-Powered Text Summarization",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)