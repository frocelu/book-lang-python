---
layout: page
title: Package - libglib2.0-dev
description: >
  Package - libglib2.0-dev
date: 2017-04-03 18:44:15 +0800
source_url: '/read/subject/gi/package-exploration/libglib2.0-dev.md'
parent:
  title: Python PyGObject (PyGI)
  url: '/read/subject/gi/'
---


# libglib2.0-dev

執行

``` sh
$ apt-cache show libglib2.0-dev
```

執行

``` sh
$ apt-cache showsrc libglib2.0-dev
```

執行

``` sh
$ apt-cache show libglib2.0-dev | grep '^Depends:'
```

顯示

```
Depends: libc6 (>= 2.4), libglib2.0-0 (= 2.48.2-0ubuntu1), python:any (>= 2.6.6-7~), libglib2.0-bin (= 2.48.2-0ubuntu1), libpcre3-dev (>= 1:8.31), pkg-config, zlib1g-dev
```

執行

``` sh
$ apt-cache showsrc libglib2.0-dev | grep '^Binary:' -B 1 -A 1
```

顯示

```
Package: glib2.0
Binary: libglib2.0-0, libglib2.0-tests, libglib2.0-udeb, libglib2.0-bin, libglib2.0-dev, libglib2.0-0-dbg, libglib2.0-data, libglib2.0-doc, libgio-fam, libglib2.0-0-refdbg
Version: 2.48.0-1ubuntu4
```

執行

``` sh
$ dpkg -l libglib2.0-dev
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  libglib2.0-dev                  2.48.2-0ubuntu1      amd64                Development files for the GLib library
```

執行

``` sh
$ dpkg -L libglib2.0-dev | sort
```

顯示

```
/.
/usr
/usr/bin
/usr/bin/gdbus-codegen
/usr/bin/glib-genmarshal
/usr/bin/glib-gettextize
/usr/bin/glib-mkenums
/usr/bin/gobject-query
/usr/bin/gtester
/usr/bin/gtester-report
/usr/include
/usr/include/gio-unix-2.0
/usr/include/gio-unix-2.0/gio
/usr/include/gio-unix-2.0/gio/gdesktopappinfo.h
/usr/include/gio-unix-2.0/gio/gfiledescriptorbased.h
/usr/include/gio-unix-2.0/gio/gunixconnection.h
/usr/include/gio-unix-2.0/gio/gunixcredentialsmessage.h
/usr/include/gio-unix-2.0/gio/gunixfdlist.h
/usr/include/gio-unix-2.0/gio/gunixfdmessage.h
/usr/include/gio-unix-2.0/gio/gunixinputstream.h
/usr/include/gio-unix-2.0/gio/gunixmounts.h
/usr/include/gio-unix-2.0/gio/gunixoutputstream.h
/usr/include/gio-unix-2.0/gio/gunixsocketaddress.h
/usr/include/glib-2.0
/usr/include/glib-2.0/gio
/usr/include/glib-2.0/gio/gactiongroupexporter.h
/usr/include/glib-2.0/gio/gactiongroup.h
/usr/include/glib-2.0/gio/gaction.h
/usr/include/glib-2.0/gio/gactionmap.h
/usr/include/glib-2.0/gio/gappinfo.h
/usr/include/glib-2.0/gio/gapplicationcommandline.h
/usr/include/glib-2.0/gio/gapplication.h
/usr/include/glib-2.0/gio/gasyncinitable.h
/usr/include/glib-2.0/gio/gasyncresult.h
/usr/include/glib-2.0/gio/gbufferedinputstream.h
/usr/include/glib-2.0/gio/gbufferedoutputstream.h
/usr/include/glib-2.0/gio/gbytesicon.h
/usr/include/glib-2.0/gio/gcancellable.h
/usr/include/glib-2.0/gio/gcharsetconverter.h
/usr/include/glib-2.0/gio/gcontenttype.h
/usr/include/glib-2.0/gio/gconverter.h
/usr/include/glib-2.0/gio/gconverterinputstream.h
/usr/include/glib-2.0/gio/gconverteroutputstream.h
/usr/include/glib-2.0/gio/gcredentials.h
/usr/include/glib-2.0/gio/gdatagrambased.h
/usr/include/glib-2.0/gio/gdatainputstream.h
/usr/include/glib-2.0/gio/gdataoutputstream.h
/usr/include/glib-2.0/gio/gdbusactiongroup.h
/usr/include/glib-2.0/gio/gdbusaddress.h
/usr/include/glib-2.0/gio/gdbusauthobserver.h
/usr/include/glib-2.0/gio/gdbusconnection.h
/usr/include/glib-2.0/gio/gdbuserror.h
/usr/include/glib-2.0/gio/gdbusinterface.h
/usr/include/glib-2.0/gio/gdbusinterfaceskeleton.h
/usr/include/glib-2.0/gio/gdbusintrospection.h
/usr/include/glib-2.0/gio/gdbusmenumodel.h
/usr/include/glib-2.0/gio/gdbusmessage.h
/usr/include/glib-2.0/gio/gdbusmethodinvocation.h
/usr/include/glib-2.0/gio/gdbusnameowning.h
/usr/include/glib-2.0/gio/gdbusnamewatching.h
/usr/include/glib-2.0/gio/gdbusobject.h
/usr/include/glib-2.0/gio/gdbusobjectmanagerclient.h
/usr/include/glib-2.0/gio/gdbusobjectmanager.h
/usr/include/glib-2.0/gio/gdbusobjectmanagerserver.h
/usr/include/glib-2.0/gio/gdbusobjectproxy.h
/usr/include/glib-2.0/gio/gdbusobjectskeleton.h
/usr/include/glib-2.0/gio/gdbusproxy.h
/usr/include/glib-2.0/gio/gdbusserver.h
/usr/include/glib-2.0/gio/gdbusutils.h
/usr/include/glib-2.0/gio/gdrive.h
/usr/include/glib-2.0/gio/gdtlsclientconnection.h
/usr/include/glib-2.0/gio/gdtlsconnection.h
/usr/include/glib-2.0/gio/gdtlsserverconnection.h
/usr/include/glib-2.0/gio/gemblemedicon.h
/usr/include/glib-2.0/gio/gemblem.h
/usr/include/glib-2.0/gio/gfileattribute.h
/usr/include/glib-2.0/gio/gfileenumerator.h
/usr/include/glib-2.0/gio/gfile.h
/usr/include/glib-2.0/gio/gfileicon.h
/usr/include/glib-2.0/gio/gfileinfo.h
/usr/include/glib-2.0/gio/gfileinputstream.h
/usr/include/glib-2.0/gio/gfileiostream.h
/usr/include/glib-2.0/gio/gfilemonitor.h
/usr/include/glib-2.0/gio/gfilenamecompleter.h
/usr/include/glib-2.0/gio/gfileoutputstream.h
/usr/include/glib-2.0/gio/gfilterinputstream.h
/usr/include/glib-2.0/gio/gfilteroutputstream.h
/usr/include/glib-2.0/gio/gicon.h
/usr/include/glib-2.0/gio/ginetaddress.h
/usr/include/glib-2.0/gio/ginetaddressmask.h
/usr/include/glib-2.0/gio/ginetsocketaddress.h
/usr/include/glib-2.0/gio/ginitable.h
/usr/include/glib-2.0/gio/ginputstream.h
/usr/include/glib-2.0/gio/gio-autocleanups.h
/usr/include/glib-2.0/gio/gioenums.h
/usr/include/glib-2.0/gio/gioenumtypes.h
/usr/include/glib-2.0/gio/gioerror.h
/usr/include/glib-2.0/gio/gio.h
/usr/include/glib-2.0/gio/giomodule.h
/usr/include/glib-2.0/gio/gioscheduler.h
/usr/include/glib-2.0/gio/giostream.h
/usr/include/glib-2.0/gio/giotypes.h
/usr/include/glib-2.0/gio/glistmodel.h
/usr/include/glib-2.0/gio/gliststore.h
/usr/include/glib-2.0/gio/gloadableicon.h
/usr/include/glib-2.0/gio/gmemoryinputstream.h
/usr/include/glib-2.0/gio/gmemoryoutputstream.h
/usr/include/glib-2.0/gio/gmenuexporter.h
/usr/include/glib-2.0/gio/gmenu.h
/usr/include/glib-2.0/gio/gmenumodel.h
/usr/include/glib-2.0/gio/gmount.h
/usr/include/glib-2.0/gio/gmountoperation.h
/usr/include/glib-2.0/gio/gnativevolumemonitor.h
/usr/include/glib-2.0/gio/gnetworkaddress.h
/usr/include/glib-2.0/gio/gnetworking.h
/usr/include/glib-2.0/gio/gnetworkmonitor.h
/usr/include/glib-2.0/gio/gnetworkservice.h
/usr/include/glib-2.0/gio/gnotification.h
/usr/include/glib-2.0/gio/goutputstream.h
/usr/include/glib-2.0/gio/gpermission.h
/usr/include/glib-2.0/gio/gpollableinputstream.h
/usr/include/glib-2.0/gio/gpollableoutputstream.h
/usr/include/glib-2.0/gio/gpollableutils.h
/usr/include/glib-2.0/gio/gpropertyaction.h
/usr/include/glib-2.0/gio/gproxyaddressenumerator.h
/usr/include/glib-2.0/gio/gproxyaddress.h
/usr/include/glib-2.0/gio/gproxy.h
/usr/include/glib-2.0/gio/gproxyresolver.h
/usr/include/glib-2.0/gio/gremoteactiongroup.h
/usr/include/glib-2.0/gio/gresolver.h
/usr/include/glib-2.0/gio/gresource.h
/usr/include/glib-2.0/gio/gseekable.h
/usr/include/glib-2.0/gio/gsettingsbackend.h
/usr/include/glib-2.0/gio/gsettings.h
/usr/include/glib-2.0/gio/gsettingsschema.h
/usr/include/glib-2.0/gio/gsimpleactiongroup.h
/usr/include/glib-2.0/gio/gsimpleaction.h
/usr/include/glib-2.0/gio/gsimpleasyncresult.h
/usr/include/glib-2.0/gio/gsimpleiostream.h
/usr/include/glib-2.0/gio/gsimplepermission.h
/usr/include/glib-2.0/gio/gsimpleproxyresolver.h
/usr/include/glib-2.0/gio/gsocketaddressenumerator.h
/usr/include/glib-2.0/gio/gsocketaddress.h
/usr/include/glib-2.0/gio/gsocketclient.h
/usr/include/glib-2.0/gio/gsocketconnectable.h
/usr/include/glib-2.0/gio/gsocketconnection.h
/usr/include/glib-2.0/gio/gsocketcontrolmessage.h
/usr/include/glib-2.0/gio/gsocket.h
/usr/include/glib-2.0/gio/gsocketlistener.h
/usr/include/glib-2.0/gio/gsocketservice.h
/usr/include/glib-2.0/gio/gsrvtarget.h
/usr/include/glib-2.0/gio/gsubprocess.h
/usr/include/glib-2.0/gio/gsubprocesslauncher.h
/usr/include/glib-2.0/gio/gtask.h
/usr/include/glib-2.0/gio/gtcpconnection.h
/usr/include/glib-2.0/gio/gtcpwrapperconnection.h
/usr/include/glib-2.0/gio/gtestdbus.h
/usr/include/glib-2.0/gio/gthemedicon.h
/usr/include/glib-2.0/gio/gthreadedsocketservice.h
/usr/include/glib-2.0/gio/gtlsbackend.h
/usr/include/glib-2.0/gio/gtlscertificate.h
/usr/include/glib-2.0/gio/gtlsclientconnection.h
/usr/include/glib-2.0/gio/gtlsconnection.h
/usr/include/glib-2.0/gio/gtlsdatabase.h
/usr/include/glib-2.0/gio/gtlsfiledatabase.h
/usr/include/glib-2.0/gio/gtlsinteraction.h
/usr/include/glib-2.0/gio/gtlspassword.h
/usr/include/glib-2.0/gio/gtlsserverconnection.h
/usr/include/glib-2.0/gio/gvfs.h
/usr/include/glib-2.0/gio/gvolume.h
/usr/include/glib-2.0/gio/gvolumemonitor.h
/usr/include/glib-2.0/gio/gzlibcompressor.h
/usr/include/glib-2.0/gio/gzlibdecompressor.h
/usr/include/glib-2.0/glib
/usr/include/glib-2.0/glib/deprecated
/usr/include/glib-2.0/glib/deprecated/gallocator.h
/usr/include/glib-2.0/glib/deprecated/gcache.h
/usr/include/glib-2.0/glib/deprecated/gcompletion.h
/usr/include/glib-2.0/glib/deprecated/gmain.h
/usr/include/glib-2.0/glib/deprecated/grel.h
/usr/include/glib-2.0/glib/deprecated/gthread.h
/usr/include/glib-2.0/glib/galloca.h
/usr/include/glib-2.0/glib/garray.h
/usr/include/glib-2.0/glib/gasyncqueue.h
/usr/include/glib-2.0/glib/gatomic.h
/usr/include/glib-2.0/glib/gbacktrace.h
/usr/include/glib-2.0/glib/gbase64.h
/usr/include/glib-2.0/glib/gbitlock.h
/usr/include/glib-2.0/glib/gbookmarkfile.h
/usr/include/glib-2.0/glib/gbytes.h
/usr/include/glib-2.0/glib/gcharset.h
/usr/include/glib-2.0/glib/gchecksum.h
/usr/include/glib-2.0/glib/gconvert.h
/usr/include/glib-2.0/glib/gdataset.h
/usr/include/glib-2.0/glib/gdate.h
/usr/include/glib-2.0/glib/gdatetime.h
/usr/include/glib-2.0/glib/gdir.h
/usr/include/glib-2.0/glib/genviron.h
/usr/include/glib-2.0/glib/gerror.h
/usr/include/glib-2.0/glib/gfileutils.h
/usr/include/glib-2.0/glib/ggettext.h
/usr/include/glib-2.0/glib/ghash.h
/usr/include/glib-2.0/glib/ghmac.h
/usr/include/glib-2.0/glib/ghook.h
/usr/include/glib-2.0/glib/ghostutils.h
/usr/include/glib-2.0/glib/gi18n.h
/usr/include/glib-2.0/glib/gi18n-lib.h
/usr/include/glib-2.0/glib/giochannel.h
/usr/include/glib-2.0/glib/gkeyfile.h
/usr/include/glib-2.0/glib/glib-autocleanups.h
/usr/include/glib-2.0/glib/glist.h
/usr/include/glib-2.0/glib/gmacros.h
/usr/include/glib-2.0/glib/gmain.h
/usr/include/glib-2.0/glib/gmappedfile.h
/usr/include/glib-2.0/glib/gmarkup.h
/usr/include/glib-2.0/glib/gmem.h
/usr/include/glib-2.0/glib/gmessages.h
/usr/include/glib-2.0/glib/gnode.h
/usr/include/glib-2.0/glib/goption.h
/usr/include/glib-2.0/glib/gpattern.h
/usr/include/glib-2.0/glib/gpoll.h
/usr/include/glib-2.0/glib/gprimes.h
/usr/include/glib-2.0/glib/gprintf.h
/usr/include/glib-2.0/glib/gqsort.h
/usr/include/glib-2.0/glib/gquark.h
/usr/include/glib-2.0/glib/gqueue.h
/usr/include/glib-2.0/glib/grand.h
/usr/include/glib-2.0/glib/gregex.h
/usr/include/glib-2.0/glib/gscanner.h
/usr/include/glib-2.0/glib/gsequence.h
/usr/include/glib-2.0/glib/gshell.h
/usr/include/glib-2.0/glib/gslice.h
/usr/include/glib-2.0/glib/gslist.h
/usr/include/glib-2.0/glib/gspawn.h
/usr/include/glib-2.0/glib/gstdio.h
/usr/include/glib-2.0/glib/gstrfuncs.h
/usr/include/glib-2.0/glib/gstringchunk.h
/usr/include/glib-2.0/glib/gstring.h
/usr/include/glib-2.0/glib/gtestutils.h
/usr/include/glib-2.0/glib/gthread.h
/usr/include/glib-2.0/glib/gthreadpool.h
/usr/include/glib-2.0/glib/gtimer.h
/usr/include/glib-2.0/glib/gtimezone.h
/usr/include/glib-2.0/glib/gtrashstack.h
/usr/include/glib-2.0/glib/gtree.h
/usr/include/glib-2.0/glib/gtypes.h
/usr/include/glib-2.0/glib/gunicode.h
/usr/include/glib-2.0/glib/gurifuncs.h
/usr/include/glib-2.0/glib/gutils.h
/usr/include/glib-2.0/glib/gvariant.h
/usr/include/glib-2.0/glib/gvarianttype.h
/usr/include/glib-2.0/glib/gversion.h
/usr/include/glib-2.0/glib/gversionmacros.h
/usr/include/glib-2.0/glib/gwin32.h
/usr/include/glib-2.0/glib.h
/usr/include/glib-2.0/glib-object.h
/usr/include/glib-2.0/glib-unix.h
/usr/include/glib-2.0/gmodule.h
/usr/include/glib-2.0/gobject
/usr/include/glib-2.0/gobject/gbinding.h
/usr/include/glib-2.0/gobject/gboxed.h
/usr/include/glib-2.0/gobject/gclosure.h
/usr/include/glib-2.0/gobject/genums.h
/usr/include/glib-2.0/gobject/glib-types.h
/usr/include/glib-2.0/gobject/gmarshal.h
/usr/include/glib-2.0/gobject/gobject-autocleanups.h
/usr/include/glib-2.0/gobject/gobject.h
/usr/include/glib-2.0/gobject/gobjectnotifyqueue.c
/usr/include/glib-2.0/gobject/gparam.h
/usr/include/glib-2.0/gobject/gparamspecs.h
/usr/include/glib-2.0/gobject/gsignal.h
/usr/include/glib-2.0/gobject/gsourceclosure.h
/usr/include/glib-2.0/gobject/gtype.h
/usr/include/glib-2.0/gobject/gtypemodule.h
/usr/include/glib-2.0/gobject/gtypeplugin.h
/usr/include/glib-2.0/gobject/gvaluearray.h
/usr/include/glib-2.0/gobject/gvaluecollector.h
/usr/include/glib-2.0/gobject/gvalue.h
/usr/include/glib-2.0/gobject/gvaluetypes.h
/usr/lib
/usr/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu/glib-2.0
/usr/lib/x86_64-linux-gnu/glib-2.0/include
/usr/lib/x86_64-linux-gnu/glib-2.0/include/glibconfig.h
/usr/lib/x86_64-linux-gnu/libgio-2.0.a
/usr/lib/x86_64-linux-gnu/libgio-2.0.so
/usr/lib/x86_64-linux-gnu/libglib-2.0.a
/usr/lib/x86_64-linux-gnu/libglib-2.0.so
/usr/lib/x86_64-linux-gnu/libgmodule-2.0.a
/usr/lib/x86_64-linux-gnu/libgmodule-2.0.so
/usr/lib/x86_64-linux-gnu/libgobject-2.0.a
/usr/lib/x86_64-linux-gnu/libgobject-2.0.so
/usr/lib/x86_64-linux-gnu/libgthread-2.0.a
/usr/lib/x86_64-linux-gnu/libgthread-2.0.so
/usr/lib/x86_64-linux-gnu/pkgconfig
/usr/lib/x86_64-linux-gnu/pkgconfig/gio-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gio-unix-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/glib-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gmodule-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gmodule-export-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gmodule-no-export-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gthread-2.0.pc
/usr/share
/usr/share/aclocal
/usr/share/aclocal/glib-2.0.m4
/usr/share/aclocal/glib-gettext.m4
/usr/share/aclocal/gsettings.m4
/usr/share/doc
/usr/share/doc/libglib2.0-dev
/usr/share/doc/libglib2.0-dev/AUTHORS
/usr/share/doc/libglib2.0-dev/changelog.Debian.gz
/usr/share/doc/libglib2.0-dev/copyright
/usr/share/doc/libglib2.0-dev/NEWS.gz
/usr/share/doc/libglib2.0-dev/README.Debian
/usr/share/doc/libglib2.0-dev/README.gz
/usr/share/glib-2.0
/usr/share/glib-2.0/codegen
/usr/share/glib-2.0/codegen/codegen_docbook.py
/usr/share/glib-2.0/codegen/codegen_main.py
/usr/share/glib-2.0/codegen/codegen.py
/usr/share/glib-2.0/codegen/config.py
/usr/share/glib-2.0/codegen/dbustypes.py
/usr/share/glib-2.0/codegen/__init__.py
/usr/share/glib-2.0/codegen/parser.py
/usr/share/glib-2.0/codegen/utils.py
/usr/share/glib-2.0/gettext
/usr/share/glib-2.0/gettext/po
/usr/share/glib-2.0/gettext/po/Makefile.in.in
/usr/share/glib-2.0/schemas
/usr/share/glib-2.0/schemas/gschema.dtd
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/gdbus-codegen.1.gz
/usr/share/man/man1/glib-genmarshal.1.gz
/usr/share/man/man1/glib-gettextize.1.gz
/usr/share/man/man1/glib-mkenums.1.gz
/usr/share/man/man1/gobject-query.1.gz
/usr/share/man/man1/gtester.1.gz
/usr/share/man/man1/gtester-report.1.gz
/usr/share/python
/usr/share/python/runtime.d
/usr/share/python/runtime.d/libglib2.0-dev.rtupdate
```

執行

``` sh
$ dpkg -L libglib2.0-dev | grep bin
```

顯示

```
/usr/include/glib-2.0/gobject/gbinding.h
/usr/bin
/usr/bin/gdbus-codegen
/usr/bin/gtester-report
/usr/bin/glib-mkenums
/usr/bin/glib-gettextize
/usr/bin/gtester
/usr/bin/glib-genmarshal
/usr/bin/gobject-query
```

執行

``` sh
$ dpkg -L libglib2.0-dev | grep man
```

顯示

```
/usr/include/glib-2.0/gio/gapplicationcommandline.h
/usr/include/glib-2.0/gio/gdbusobjectmanagerclient.h
/usr/include/glib-2.0/gio/gdbusobjectmanager.h
/usr/include/glib-2.0/gio/gdbusobjectmanagerserver.h
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/glib-genmarshal.1.gz
/usr/share/man/man1/gobject-query.1.gz
/usr/share/man/man1/gtester.1.gz
/usr/share/man/man1/glib-mkenums.1.gz
/usr/share/man/man1/gdbus-codegen.1.gz
/usr/share/man/man1/gtester-report.1.gz
```

執行

``` sh
$ dpkg -L libglib2.0-dev | grep pc
```

顯示

```
/usr/lib/x86_64-linux-gnu/pkgconfig/gmodule-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gio-unix-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/glib-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gmodule-no-export-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gio-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gmodule-export-2.0.pc
/usr/lib/x86_64-linux-gnu/pkgconfig/gthread-2.0.pc
/usr/include/glib-2.0/gio/gtcpconnection.h
```

根據「/usr/lib/x86_64-linux-gnu/pkgconfig/gobject-2.0.pc」，

執行

``` sh
$ pkg-config --cflags --libs gobject-2.0
```

顯示

```
-I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include -lgobject-2.0 -lglib-2.0
```

* http://helgo.net/simon/introspection-tutorial/stepfour.xhtml