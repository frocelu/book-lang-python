#!/usr/bin/env sh

## http://foreachsam.github.io/book-util-dbus/book/content/case/fcitx/basic/qdbus/

#im_name=$(qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.GetIMAddon chewing)
#echo $im_name
#qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.ConfigureAddon $im_name

qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.ConfigureAddon $(qdbus org.fcitx.Fcitx /inputmethod org.fcitx.Fcitx.InputMethod.GetIMAddon chewing)
