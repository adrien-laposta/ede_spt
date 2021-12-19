import os

from cobaya.install import download_file
from cobaya.likelihoods.base_classes import Planck2018Clik, planck_clik
from cobaya.log import get_logger


class TT_lmax650(Planck2018Clik):
    @classmethod
    def install(cls, path=None, force=False, code=True, data=True, no_progress_bars=False):
        name = cls.get_qualified_class_name()
        log = get_logger(name)
        path_names = {"code": planck_clik.common_path, "data": planck_clik.get_data_path(name)}
        import platform

        if platform.system() == "Windows":
            log.error("Not compatible with Windows.")
            return False
        if planck_clik._clik_install_failed:
            log.info("Previous clik install failed, skipping")
            return False
        # Create common folders: all planck likelihoods share install
        # folder for code and data
        paths = {}
        for s in ("code", "data"):
            if eval(s):
                paths[s] = os.path.realpath(os.path.join(path, s, path_names[s]))
                if not os.path.exists(paths[s]):
                    os.makedirs(paths[s])
        success = True
        # Install clik
        if code and (not planck_clik.is_installed_clik(paths["code"]) or force):
            log.info("Installing the clik code.")
            success *= planck_clik.install_clik(paths["code"], no_progress_bars=no_progress_bars)
            if not success:
                log.warning(
                    "clik code installation failed! "
                    "Try configuring+compiling by hand at " + paths["code"]
                )
                _clik_install_failed = True
        if data:
            # 2nd test, in case the code wasn't there but the data is:
            if force or not cls.is_installed(path=path, code=False, data=True):
                log.info("Downloading the likelihood data.")
                url = r"https://portal.nersc.gov/cfs/sobs/users/xgarrido/plik_rd12_HM_v22_TT_lmax650.clik.tar.gz"
                if not download_file(
                    url,
                    paths["data"],
                    decompress=True,
                    logger=log,
                    no_progress_bars=no_progress_bars,
                ):
                    log.error("Not possible to download this likelihood.")
                    success = False
                # Additional data and covmats, stored in same repo as the
                # 2018 python lensing likelihood
                from cobaya.likelihoods.planck_2018_lensing import native

                if not native.is_installed(data=True, path=path):
                    success *= native.install(
                        path=path,
                        force=force,
                        code=code,
                        data=data,
                        no_progress_bars=no_progress_bars,
                    )
        return success
