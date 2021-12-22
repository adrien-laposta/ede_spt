import os
import tempfile
import unittest

packages_path = os.environ.get("COBAYA_PACKAGES_PATH") or os.path.join(
    tempfile.gettempdir(), "spt_ede_packages"
)


class YamlTest(unittest.TestCase):
    def _read(self):
        from cobaya.yaml import yaml_load_file

        return yaml_load_file(self.yaml_file)

    def _install(self):
        from cobaya.install import install

        install(self._read(), path=packages_path)

    def _evaluate(self):
        from cobaya.run import run

        info = self._read()
        info["packages_path"] = packages_path
        info["sampler"] = {"evaluate": None}
        run(info)

    def test_yaml(self):

        configs = [
            "act",
            "p18",
            "spt3g",
            "spt3g_p18tt650",
            "spt3g_p18tt650_bao_lensing",
            "spt3g_p18full",
            "spt3g_act",
            "spt3g_act_p18tt650",
            "spt3g_act_p18full",
        ]
        for config in configs:
            self.yaml_file = os.path.join("../yaml", f"{config}_ede.yaml")
            self._read()
            self._install()
            self._evaluate()
