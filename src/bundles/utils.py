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
The bundles related utility methods and tools module
"""
from typing import Optional, TypeVar
from src.bundles.budgie import Budgie
from src.bundles.bundle import Bundle
from src.bundles.cinnamon import Cinnamon
from src.bundles.copyacm import CopyACM
from src.bundles.cups import Cups
from src.bundles.cutefish import Cutefish
from src.bundles.deepin import Deepin
from src.bundles.enlightenment import Enlightenment
from src.bundles.gnome import Gnome
from src.bundles.grmlzsh import GrmlZsh
from src.bundles.grub import Grub
from src.bundles.i3 import I3
from src.bundles.iwd import Iwd
from src.bundles.linux import LinuxCurrent, LinuxLts, LinuxZen, LinuxHardened
from src.bundles.lxqt import Lxqt
from src.bundles.mainfilesystems import MainFileSystems
from src.bundles.mainfonts import MainFonts
from src.bundles.mate import Mate
from src.bundles.microcodes import Microcodes
from src.bundles.networkmanager import NetworkManager
from src.bundles.nvidia import NvidiaDriver
from src.bundles.pipewire import PipeWire
from src.bundles.plasma import Plasma
from src.bundles.sway import Sway
from src.bundles.systemdnet import SystemdNet
from src.bundles.terminus import TerminusFont
from src.bundles.xfce import Xfce
from src.bundles.zram import Zram
from src.options import Kernels, BootLoaders, Desktops, Bundles, Network
from src.options import OptionEnum
from src.utils import prompt_option


def process_bundle(name: OptionEnum) -> Bundle:
    """
    Process a bundle name into a Bundle object.
    """
    match name:
        case Kernels.CURRENT:
            bundle = LinuxCurrent(name)
        case Kernels.LTS:
            bundle = LinuxLts(name)
        case Kernels.ZEN:
            bundle = LinuxZen(name)
        case Kernels.HARDENED:
            bundle = LinuxHardened(name)
        case BootLoaders.GRUB:
            bundle = Grub(name)
        case Desktops.GNOME:
            bundle = Gnome(name)
        case Desktops.PLASMA:
            bundle = Plasma(name)
        case Desktops.XFCE:
            bundle = Xfce(name)
        case Desktops.BUDGIE:
            bundle = Budgie(name)
        case Desktops.CINNAMON:
            bundle = Cinnamon(name)
        case Desktops.CUTEFISH:
            bundle = Cutefish(name)
        case Desktops.DEEPIN:
            bundle = Deepin(name)
        case Desktops.LXQT:
            bundle = Lxqt(name)
        case Desktops.MATE:
            bundle = Mate(name)
        case Desktops.ENLIGHTENMENT:
            bundle = Enlightenment(name)
        case Desktops.I3:
            bundle = I3(name)
        case Desktops.SWAY:
            bundle = Sway(name)
        case Network.NETWORK_MANAGER:
            bundle = NetworkManager(name)
        case Network.IWD:
            bundle = Iwd(name)
        case Network.SYSTEMD:
            bundle = SystemdNet(name)
        case Bundles.CUPS:
            bundle = Cups(name)
        case Bundles.GRML:
            bundle = GrmlZsh(name)
        case Bundles.MAIN_FILE_SYSTEMS:
            bundle = MainFileSystems(name)
        case Bundles.MAIN_FONTS:
            bundle = MainFonts(name)
        case Bundles.MICROCODES:
            bundle = Microcodes()
        case Bundles.NVIDIA:
            bundle = NvidiaDriver(name)
        case Bundles.PIPEWIRE:
            bundle = PipeWire(name)
        case Bundles.TERMINUS:
            bundle = TerminusFont(name)
        case Bundles.ZRAM:
            bundle = Zram(name)
        case Bundles.COPY_ACM:
            bundle = CopyACM(name)
        case _:
            bundle = Bundle(name)
    return bundle


T = TypeVar("T", bound=OptionEnum)


def prompt_bundle(
    message: str,
    error_msg: str,
    options: type[T],
    supported_msg: Optional[str],
    default: Optional[T],
    *ignores: T,
    new_line_prompt: bool = True,
) -> Bundle:
    """
    A method to prompt for a bundle.
    """
    option = prompt_option(
        message,
        error_msg,
        options,
        supported_msg,
        default,
        *ignores,
        new_line_prompt=new_line_prompt,
    )
    if not option:
        raise ValueError("No bundle selected")
    bundle = process_bundle(option)
    bundle.prompt_extra()
    return bundle
