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
The systemd network bundle module
"""

from src.bundles.bundle import Bundle
from src.i18n import I18n
from src.partitioninginfo import PartitioningInfo
from src.prelaunchinfo import PreLaunchInfo
from src.systeminfo import SystemInfo
from src.utils import print_sub_step, execute

_ = I18n().gettext


class SystemdNet(Bundle):
    """
    Grml ZSH config class.
    """

    def packages(self, system_info: SystemInfo) -> list[str]:
        return ["systemd-resolvconf"]

    def print_resume(self):
        print_sub_step(_("Enable systemd network stack."))

    def configure(
        self,
        system_info: SystemInfo,
        pre_launch_info: PreLaunchInfo,
        partitioning_info: PartitioningInfo,
    ):
        execute("ln -sf /run/systemd/resolve/stub-resolv.conf /mnt/etc/resolv.conf")
        execute("cp -r /etc/systemd/network /mnt/etc/systemd/")
        execute('arch-chroot /mnt bash -c "systemctl enable systemd-networkd"')
        execute('arch-chroot /mnt bash -c "systemctl enable systemd-resolved"')
