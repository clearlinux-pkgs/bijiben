#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : bijiben
Version  : 40.1
Release  : 37
URL      : https://download.gnome.org/sources/bijiben/40/bijiben-40.1.tar.xz
Source0  : https://download.gnome.org/sources/bijiben/40/bijiben-40.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: bijiben-bin = %{version}-%{release}
Requires: bijiben-data = %{version}-%{release}
Requires: bijiben-libexec = %{version}-%{release}
Requires: bijiben-license = %{version}-%{release}
Requires: bijiben-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : curl-dev
BuildRequires : gnome-online-accounts-dev
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libecal-2.0)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(webkit2gtk-4.0)
BuildRequires : tracker-dev
BuildRequires : webkitgtk-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# GNOME Notes
GNOME Notes, formerly "Bijiben", is a note editor designed to remain simple to use.
(筆記本 / 笔记本 / bijiben means "notebook".)

%package bin
Summary: bin components for the bijiben package.
Group: Binaries
Requires: bijiben-data = %{version}-%{release}
Requires: bijiben-libexec = %{version}-%{release}
Requires: bijiben-license = %{version}-%{release}

%description bin
bin components for the bijiben package.


%package data
Summary: data components for the bijiben package.
Group: Data

%description data
data components for the bijiben package.


%package doc
Summary: doc components for the bijiben package.
Group: Documentation

%description doc
doc components for the bijiben package.


%package libexec
Summary: libexec components for the bijiben package.
Group: Default
Requires: bijiben-license = %{version}-%{release}

%description libexec
libexec components for the bijiben package.


%package license
Summary: license components for the bijiben package.
Group: Default

%description license
license components for the bijiben package.


%package locales
Summary: locales components for the bijiben package.
Group: Default

%description locales
locales components for the bijiben package.


%prep
%setup -q -n bijiben-40.1
cd %{_builddir}/bijiben-40.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680018512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/bijiben
cp %{_builddir}/bijiben-%{version}/COPYING %{buildroot}/usr/share/package-licenses/bijiben/338650eb7a42dd9bc1f1c6961420f2633b24932d || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang bijiben

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bijiben

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Notes.desktop
/usr/share/bijiben/Default.css
/usr/share/bijiben/bijiben.js
/usr/share/bijiben/icons/hicolor/16x16/actions/note.png
/usr/share/bijiben/icons/hicolor/24x24/actions/note.png
/usr/share/bijiben/icons/hicolor/48x48/actions/note.png
/usr/share/bijiben/icons/hicolor/symbolic/actions/link-symbolic.svg
/usr/share/dbus-1/services/org.gnome.Notes.SearchProvider.service
/usr/share/glib-2.0/schemas/org.gnome.Notes.gschema.xml
/usr/share/gnome-shell/search-providers/org.gnome.Notes-search-provider.ini
/usr/share/icons/hicolor/scalable/apps/org.gnome.Notes.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Notes-symbolic.svg
/usr/share/metainfo/org.gnome.Notes.appdata.xml
/usr/share/mime-packages/org.gnome.Notes.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/bijiben/colors.page
/usr/share/help/C/bijiben/create.page
/usr/share/help/C/bijiben/cut-copy-paste.page
/usr/share/help/C/bijiben/delete-permanent.page
/usr/share/help/C/bijiben/delete-restore.page
/usr/share/help/C/bijiben/delete.page
/usr/share/help/C/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/C/bijiben/figures/notes-3-36.png
/usr/share/help/C/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/C/bijiben/format-list.page
/usr/share/help/C/bijiben/format-text.page
/usr/share/help/C/bijiben/index.page
/usr/share/help/C/bijiben/introduction.page
/usr/share/help/C/bijiben/legal.xml
/usr/share/help/C/bijiben/new-window.page
/usr/share/help/C/bijiben/notebooks.page
/usr/share/help/C/bijiben/rename.page
/usr/share/help/C/bijiben/search.page
/usr/share/help/C/bijiben/share.page
/usr/share/help/ca/bijiben/colors.page
/usr/share/help/ca/bijiben/create.page
/usr/share/help/ca/bijiben/cut-copy-paste.page
/usr/share/help/ca/bijiben/delete-permanent.page
/usr/share/help/ca/bijiben/delete-restore.page
/usr/share/help/ca/bijiben/delete.page
/usr/share/help/ca/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/ca/bijiben/figures/notes-3-36.png
/usr/share/help/ca/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/ca/bijiben/format-list.page
/usr/share/help/ca/bijiben/format-text.page
/usr/share/help/ca/bijiben/index.page
/usr/share/help/ca/bijiben/introduction.page
/usr/share/help/ca/bijiben/legal.xml
/usr/share/help/ca/bijiben/new-window.page
/usr/share/help/ca/bijiben/notebooks.page
/usr/share/help/ca/bijiben/rename.page
/usr/share/help/ca/bijiben/search.page
/usr/share/help/ca/bijiben/share.page
/usr/share/help/cs/bijiben/colors.page
/usr/share/help/cs/bijiben/create.page
/usr/share/help/cs/bijiben/cut-copy-paste.page
/usr/share/help/cs/bijiben/delete-permanent.page
/usr/share/help/cs/bijiben/delete-restore.page
/usr/share/help/cs/bijiben/delete.page
/usr/share/help/cs/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/cs/bijiben/figures/notes-3-36.png
/usr/share/help/cs/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/cs/bijiben/format-list.page
/usr/share/help/cs/bijiben/format-text.page
/usr/share/help/cs/bijiben/index.page
/usr/share/help/cs/bijiben/introduction.page
/usr/share/help/cs/bijiben/legal.xml
/usr/share/help/cs/bijiben/new-window.page
/usr/share/help/cs/bijiben/notebooks.page
/usr/share/help/cs/bijiben/rename.page
/usr/share/help/cs/bijiben/search.page
/usr/share/help/cs/bijiben/share.page
/usr/share/help/de/bijiben/colors.page
/usr/share/help/de/bijiben/create.page
/usr/share/help/de/bijiben/cut-copy-paste.page
/usr/share/help/de/bijiben/delete-permanent.page
/usr/share/help/de/bijiben/delete-restore.page
/usr/share/help/de/bijiben/delete.page
/usr/share/help/de/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/de/bijiben/figures/notes-3-36.png
/usr/share/help/de/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/de/bijiben/format-list.page
/usr/share/help/de/bijiben/format-text.page
/usr/share/help/de/bijiben/index.page
/usr/share/help/de/bijiben/introduction.page
/usr/share/help/de/bijiben/legal.xml
/usr/share/help/de/bijiben/new-window.page
/usr/share/help/de/bijiben/notebooks.page
/usr/share/help/de/bijiben/rename.page
/usr/share/help/de/bijiben/search.page
/usr/share/help/de/bijiben/share.page
/usr/share/help/el/bijiben/colors.page
/usr/share/help/el/bijiben/create.page
/usr/share/help/el/bijiben/cut-copy-paste.page
/usr/share/help/el/bijiben/delete-permanent.page
/usr/share/help/el/bijiben/delete-restore.page
/usr/share/help/el/bijiben/delete.page
/usr/share/help/el/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/el/bijiben/figures/notes-3-36.png
/usr/share/help/el/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/el/bijiben/format-list.page
/usr/share/help/el/bijiben/format-text.page
/usr/share/help/el/bijiben/index.page
/usr/share/help/el/bijiben/introduction.page
/usr/share/help/el/bijiben/legal.xml
/usr/share/help/el/bijiben/new-window.page
/usr/share/help/el/bijiben/notebooks.page
/usr/share/help/el/bijiben/rename.page
/usr/share/help/el/bijiben/search.page
/usr/share/help/el/bijiben/share.page
/usr/share/help/es/bijiben/colors.page
/usr/share/help/es/bijiben/create.page
/usr/share/help/es/bijiben/cut-copy-paste.page
/usr/share/help/es/bijiben/delete-permanent.page
/usr/share/help/es/bijiben/delete-restore.page
/usr/share/help/es/bijiben/delete.page
/usr/share/help/es/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/es/bijiben/figures/notes-3-36.png
/usr/share/help/es/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/es/bijiben/format-list.page
/usr/share/help/es/bijiben/format-text.page
/usr/share/help/es/bijiben/index.page
/usr/share/help/es/bijiben/introduction.page
/usr/share/help/es/bijiben/legal.xml
/usr/share/help/es/bijiben/new-window.page
/usr/share/help/es/bijiben/notebooks.page
/usr/share/help/es/bijiben/rename.page
/usr/share/help/es/bijiben/search.page
/usr/share/help/es/bijiben/share.page
/usr/share/help/eu/bijiben/colors.page
/usr/share/help/eu/bijiben/create.page
/usr/share/help/eu/bijiben/cut-copy-paste.page
/usr/share/help/eu/bijiben/delete-permanent.page
/usr/share/help/eu/bijiben/delete-restore.page
/usr/share/help/eu/bijiben/delete.page
/usr/share/help/eu/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/eu/bijiben/figures/notes-3-36.png
/usr/share/help/eu/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/eu/bijiben/format-list.page
/usr/share/help/eu/bijiben/format-text.page
/usr/share/help/eu/bijiben/index.page
/usr/share/help/eu/bijiben/introduction.page
/usr/share/help/eu/bijiben/legal.xml
/usr/share/help/eu/bijiben/new-window.page
/usr/share/help/eu/bijiben/notebooks.page
/usr/share/help/eu/bijiben/rename.page
/usr/share/help/eu/bijiben/search.page
/usr/share/help/eu/bijiben/share.page
/usr/share/help/fr/bijiben/colors.page
/usr/share/help/fr/bijiben/create.page
/usr/share/help/fr/bijiben/cut-copy-paste.page
/usr/share/help/fr/bijiben/delete-permanent.page
/usr/share/help/fr/bijiben/delete-restore.page
/usr/share/help/fr/bijiben/delete.page
/usr/share/help/fr/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/fr/bijiben/figures/notes-3-36.png
/usr/share/help/fr/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/fr/bijiben/format-list.page
/usr/share/help/fr/bijiben/format-text.page
/usr/share/help/fr/bijiben/index.page
/usr/share/help/fr/bijiben/introduction.page
/usr/share/help/fr/bijiben/legal.xml
/usr/share/help/fr/bijiben/new-window.page
/usr/share/help/fr/bijiben/notebooks.page
/usr/share/help/fr/bijiben/rename.page
/usr/share/help/fr/bijiben/search.page
/usr/share/help/fr/bijiben/share.page
/usr/share/help/fur/bijiben/colors.page
/usr/share/help/fur/bijiben/create.page
/usr/share/help/fur/bijiben/cut-copy-paste.page
/usr/share/help/fur/bijiben/delete-permanent.page
/usr/share/help/fur/bijiben/delete-restore.page
/usr/share/help/fur/bijiben/delete.page
/usr/share/help/fur/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/fur/bijiben/figures/notes-3-36.png
/usr/share/help/fur/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/fur/bijiben/format-list.page
/usr/share/help/fur/bijiben/format-text.page
/usr/share/help/fur/bijiben/index.page
/usr/share/help/fur/bijiben/introduction.page
/usr/share/help/fur/bijiben/legal.xml
/usr/share/help/fur/bijiben/new-window.page
/usr/share/help/fur/bijiben/notebooks.page
/usr/share/help/fur/bijiben/rename.page
/usr/share/help/fur/bijiben/search.page
/usr/share/help/fur/bijiben/share.page
/usr/share/help/hu/bijiben/colors.page
/usr/share/help/hu/bijiben/create.page
/usr/share/help/hu/bijiben/cut-copy-paste.page
/usr/share/help/hu/bijiben/delete-permanent.page
/usr/share/help/hu/bijiben/delete-restore.page
/usr/share/help/hu/bijiben/delete.page
/usr/share/help/hu/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/hu/bijiben/figures/notes-3-36.png
/usr/share/help/hu/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/hu/bijiben/format-list.page
/usr/share/help/hu/bijiben/format-text.page
/usr/share/help/hu/bijiben/index.page
/usr/share/help/hu/bijiben/introduction.page
/usr/share/help/hu/bijiben/legal.xml
/usr/share/help/hu/bijiben/new-window.page
/usr/share/help/hu/bijiben/notebooks.page
/usr/share/help/hu/bijiben/rename.page
/usr/share/help/hu/bijiben/search.page
/usr/share/help/hu/bijiben/share.page
/usr/share/help/id/bijiben/colors.page
/usr/share/help/id/bijiben/create.page
/usr/share/help/id/bijiben/cut-copy-paste.page
/usr/share/help/id/bijiben/delete-permanent.page
/usr/share/help/id/bijiben/delete-restore.page
/usr/share/help/id/bijiben/delete.page
/usr/share/help/id/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/id/bijiben/figures/notes-3-36.png
/usr/share/help/id/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/id/bijiben/format-list.page
/usr/share/help/id/bijiben/format-text.page
/usr/share/help/id/bijiben/index.page
/usr/share/help/id/bijiben/introduction.page
/usr/share/help/id/bijiben/legal.xml
/usr/share/help/id/bijiben/new-window.page
/usr/share/help/id/bijiben/notebooks.page
/usr/share/help/id/bijiben/rename.page
/usr/share/help/id/bijiben/search.page
/usr/share/help/id/bijiben/share.page
/usr/share/help/ko/bijiben/colors.page
/usr/share/help/ko/bijiben/create.page
/usr/share/help/ko/bijiben/cut-copy-paste.page
/usr/share/help/ko/bijiben/delete-permanent.page
/usr/share/help/ko/bijiben/delete-restore.page
/usr/share/help/ko/bijiben/delete.page
/usr/share/help/ko/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/ko/bijiben/figures/notes-3-36.png
/usr/share/help/ko/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/ko/bijiben/format-list.page
/usr/share/help/ko/bijiben/format-text.page
/usr/share/help/ko/bijiben/index.page
/usr/share/help/ko/bijiben/introduction.page
/usr/share/help/ko/bijiben/legal.xml
/usr/share/help/ko/bijiben/new-window.page
/usr/share/help/ko/bijiben/notebooks.page
/usr/share/help/ko/bijiben/rename.page
/usr/share/help/ko/bijiben/search.page
/usr/share/help/ko/bijiben/share.page
/usr/share/help/pl/bijiben/colors.page
/usr/share/help/pl/bijiben/create.page
/usr/share/help/pl/bijiben/cut-copy-paste.page
/usr/share/help/pl/bijiben/delete-permanent.page
/usr/share/help/pl/bijiben/delete-restore.page
/usr/share/help/pl/bijiben/delete.page
/usr/share/help/pl/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/pl/bijiben/figures/notes-3-36.png
/usr/share/help/pl/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/pl/bijiben/format-list.page
/usr/share/help/pl/bijiben/format-text.page
/usr/share/help/pl/bijiben/index.page
/usr/share/help/pl/bijiben/introduction.page
/usr/share/help/pl/bijiben/legal.xml
/usr/share/help/pl/bijiben/new-window.page
/usr/share/help/pl/bijiben/notebooks.page
/usr/share/help/pl/bijiben/rename.page
/usr/share/help/pl/bijiben/search.page
/usr/share/help/pl/bijiben/share.page
/usr/share/help/pt_BR/bijiben/colors.page
/usr/share/help/pt_BR/bijiben/create.page
/usr/share/help/pt_BR/bijiben/cut-copy-paste.page
/usr/share/help/pt_BR/bijiben/delete-permanent.page
/usr/share/help/pt_BR/bijiben/delete-restore.page
/usr/share/help/pt_BR/bijiben/delete.page
/usr/share/help/pt_BR/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/pt_BR/bijiben/figures/notes-3-36.png
/usr/share/help/pt_BR/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/pt_BR/bijiben/format-list.page
/usr/share/help/pt_BR/bijiben/format-text.page
/usr/share/help/pt_BR/bijiben/index.page
/usr/share/help/pt_BR/bijiben/introduction.page
/usr/share/help/pt_BR/bijiben/legal.xml
/usr/share/help/pt_BR/bijiben/new-window.page
/usr/share/help/pt_BR/bijiben/notebooks.page
/usr/share/help/pt_BR/bijiben/rename.page
/usr/share/help/pt_BR/bijiben/search.page
/usr/share/help/pt_BR/bijiben/share.page
/usr/share/help/sv/bijiben/colors.page
/usr/share/help/sv/bijiben/create.page
/usr/share/help/sv/bijiben/cut-copy-paste.page
/usr/share/help/sv/bijiben/delete-permanent.page
/usr/share/help/sv/bijiben/delete-restore.page
/usr/share/help/sv/bijiben/delete.page
/usr/share/help/sv/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/sv/bijiben/figures/notes-3-36.png
/usr/share/help/sv/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/sv/bijiben/format-list.page
/usr/share/help/sv/bijiben/format-text.page
/usr/share/help/sv/bijiben/index.page
/usr/share/help/sv/bijiben/introduction.page
/usr/share/help/sv/bijiben/legal.xml
/usr/share/help/sv/bijiben/new-window.page
/usr/share/help/sv/bijiben/notebooks.page
/usr/share/help/sv/bijiben/rename.page
/usr/share/help/sv/bijiben/search.page
/usr/share/help/sv/bijiben/share.page
/usr/share/help/uk/bijiben/colors.page
/usr/share/help/uk/bijiben/create.page
/usr/share/help/uk/bijiben/cut-copy-paste.page
/usr/share/help/uk/bijiben/delete-permanent.page
/usr/share/help/uk/bijiben/delete-restore.page
/usr/share/help/uk/bijiben/delete.page
/usr/share/help/uk/bijiben/figures/hicolor_apps_16x16_bijiben.png
/usr/share/help/uk/bijiben/figures/notes-3-36.png
/usr/share/help/uk/bijiben/figures/org.gnome.Notes.svg
/usr/share/help/uk/bijiben/format-list.page
/usr/share/help/uk/bijiben/format-text.page
/usr/share/help/uk/bijiben/index.page
/usr/share/help/uk/bijiben/introduction.page
/usr/share/help/uk/bijiben/legal.xml
/usr/share/help/uk/bijiben/new-window.page
/usr/share/help/uk/bijiben/notebooks.page
/usr/share/help/uk/bijiben/rename.page
/usr/share/help/uk/bijiben/search.page
/usr/share/help/uk/bijiben/share.page

%files libexec
%defattr(-,root,root,-)
/usr/libexec/bijiben-shell-search-provider

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bijiben/338650eb7a42dd9bc1f1c6961420f2633b24932d

%files locales -f bijiben.lang
%defattr(-,root,root,-)

