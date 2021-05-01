from setuptools import find_packages, setup

setup(
    name="mydbot",
    version="0.1",
    description="hmmm",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Datavorous/sbutilcog",
    author="Datavorous",
    author_email="digestingdata1@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="Discord Bot, Discord, Discord Cogs",
    packages=find_packages(),
    install_requires=["discord.py","asyncio","sbutilcog", "sbfuncog", "sblycog", "sberrorcog","ModCog","FunCog"],
)

