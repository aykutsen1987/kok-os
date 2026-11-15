#!/usr/bin/env python3
# Kök OS: kurulumdan sonra hedef sistemde son ayarlar (GRUB'da diğer işletim sistemleri, canlı oturum kalıntıları)
import libcalamares


def pretty_name():
    return "Kök OS son ayarlar"


def run():
    kod = libcalamares.utils.target_env_call(["/usr/local/sbin/kok-kurulum-bitir"])
    if kod != 0:
        libcalamares.utils.warning("kok-kurulum-bitir cikis kodu: {}".format(kod))
    return None
