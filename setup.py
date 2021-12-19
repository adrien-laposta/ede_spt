from setuptools import setup

setup(
    name="ede_spt",
    version="0.1",
    python_requires=">=3.5",
    install_requires=[
        "spt @ git+https://github.com/xgarrido/spt_likelihoods@master#egg=spt_likelihoods",
        "pyactlike @ git+https://github.com/ACTCollaboration/pyactlike@master#egg=pyactlike",
        "cobaya>=3.1.0",
        "camb",
    ],
)
