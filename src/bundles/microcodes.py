"""
The microcodes auto-installation bundle module
"""
import re
from typing import Optional

from src.bundles.bundle import Bundle
from src.i18n import I18n
from src.options import Bundles
from src.systeminfo import SystemInfo
from src.utils import print_sub_step, execute

_ = I18n().gettext


class Microcodes(Bundle):
    """
    The Microcodes class.
    """

    def __init__(self):
        super().__init__(Bundles.MICROCODES)
        cpu_info_vendor = execute(
            'grep </proc/cpuinfo "vendor" | uniq', force=True, capture_output=True
        ).output
        if cpu_info_vendor:
            self.microcode_name = re.sub("\\s+", "", cpu_info_vendor).split(":")[1]
        else:
            self.microcode_name = None

    def packages(self, system_info: SystemInfo) -> list[str]:
        if self.microcode_name == "GenuineIntel":
            return ["intel-ucode"]
        if self.microcode_name == "AuthenticAMD":
            return ["amd-ucode"]
        return []

    def microcode_img(self) -> Optional[str]:
        """
        The microcode img file name retrieving method.
        """
        if self.microcode_name == "GenuineIntel":
            return "/intel-ucode.img"
        if self.microcode_name == "AuthenticAMD":
            return "/amd-ucode.img"
        return None

    def print_resume(self):
        if self.microcode_name in {"GenuineIntel", "AuthenticAMD"}:
            print_sub_step(_("Microcodes to install : %s") % self.microcode_name)
