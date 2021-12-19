import glob
import os

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install


def cp_planck_ttlmax650_to_cobaya(develop_mode=True):
    if develop_mode:
        import cobaya

        dest = cobaya.__path__[0]
    else:
        from distutils.sysconfig import get_python_lib

        dest = os.path.join(get_python_lib(), "cobaya")
    dest = os.path.join(dest, "likelihoods/planck_2018_highl_plik")

    from shutil import copy

    for f in glob.glob("./likelihoods/TT_lmax650*"):
        copy(f, dest)


class PostDevelopCommand(develop):
    """Post-command for development mode."""

    def run(self):
        develop.run(self)
        cp_planck_ttlmax650_to_cobaya(develop_mode=True)


class PostInstallCommand(install):
    """Post-command for installation mode."""

    def run(self):
        install.run(self)
        cp_planck_ttlmax650_to_cobaya(develop_mode=False)


setup(
    name="ede_spt",
    version="0.1",
    cmdclass={
        "develop": PostDevelopCommand,
        "install": PostInstallCommand,
    },
    python_requires=">=3.5",
    install_requires=[
        "spt @ git+https://github.com/xgarrido/spt_likelihoods@master#egg=spt_likelihoods",
        "pyactlike @ git+https://github.com/ACTCollaboration/pyactlike@master#egg=pyactlike",
        "cobaya>=3.1.0",
        "camb",
    ],
)
