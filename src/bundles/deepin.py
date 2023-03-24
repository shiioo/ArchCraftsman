# ArchCraftsman, The careful yet very fast Arch Linux Craftsman.
# Copyright (C) 2023 Rawleenc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
The deepin bundle module
"""

from src.bundles.bundle import Bundle
from src.i18n import I18n
from src.partitioninginfo import PartitioningInfo
from src.prelaunchinfo import PreLaunchInfo
from src.systeminfo import SystemInfo
from src.utils import print_sub_step, prompt_bool, execute

_ = I18n().gettext


class Deepin(Bundle):
    """
    Bundle class.
    """

    minimal = False

    def packages(self, system_info: SystemInfo) -> list[str]:
        packages = [
            "deepin",
            "xorg-server",
            "alsa-utils",
            "pulseaudio",
            "pulseaudio-alsa",
        ]
        if self.minimal is not True:
            packages.append("deepin-extra")
        return packages

    def print_resume(self):
        print_sub_step(_("Desktop environment : %s") % self.name)
        print_sub_step(_("Display manager : %s") % "LightDM")
        if self.minimal:
            print_sub_step(_("Install a minimal environment."))

    def prompt_extra(self):
        self.minimal = prompt_bool(
            _("Install a minimal environment ?"),
            default=False,
            help_msg=_(
                "If yes, the script will not install any extra packages, only base packages."
            ),
        )

    def configure(
        self,
        system_info: SystemInfo,
        pre_launch_info: PreLaunchInfo,
        partitioning_info: PartitioningInfo,
    ):
        execute('arch-chroot /mnt bash -c "systemctl enable lightdm"')
        execute(
            'sed -i "s|#logind-check-graphical=false|logind-check-graphical=true|g" /mnt/etc/lightdm/lightdm.conf'
        )
        pre_launch_info.setup_chroot_keyboard()
