%define		kdeplasmaver	5.22.3
%define		qtver		5.9.0
%define		kpname		kde-gtk-config
Summary:	GTK2 and GTK3 Configurator for KDE
Name:		kp5-%{kpname}
Version:	5.22.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	ef4b1bdb23e957489a9c1f0d6ead97b2
Patch0:		x32.patch
%define		specflags	-I/usr/include/harfbuzz
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK2 and GTK3 Configurator for KDE.

%prep
%setup -q -n %{kpname}-%{version}
#%%patch0 -p1

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

sed -i -e 's|/usr/bin/env sh|/bin/bash|' $RPM_BUILD_ROOT/usr/share/kconf_update/remove_window_decorations_from_gtk_css.sh

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/libexec/gtk3_preview
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/gtkconfig.so
%attr(755,root,root) %{_libdir}/kconf_update_bin/gtk_theme
%{_datadir}/kconf_update/gtkconfig.upd
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%attr(755,root,root) %{_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%attr(755,root,root) %{_datadir}/kconf_update/remove_window_decorations_from_gtk_css.sh
%{_datadir}/themes/Breeze/window_decorations.css
%dir %{_datadir}/kcm-gtk-module
%{_datadir}/kcm-gtk-module/preview.ui
