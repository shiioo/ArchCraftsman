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

from archcraftsman import info
from archcraftsman.base import execute, print_sub_step
from archcraftsman.bundles.bundle import Bundle
from archcraftsman.i18n import _
from archcraftsman.utils import prompt_bool


class Deepin(Bundle):
    """
    Bundle class.
    """

    minimal = False

    def packages(self) -> list[str]:
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

    def configure(self):
        execute('arch-chroot /mnt bash -c "systemctl enable lightdm"')
        execute(
            'sed -i "s|#logind-check-graphical=false|logind-check-graphical=true|g" /mnt/etc/lightdm/lightdm.conf'
        )
        info.ai.pre_launch_info.setup_chroot_keyboard()
