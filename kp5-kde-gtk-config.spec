%define		kdeplasmaver	5.15.3
%define		qtver		5.9.0
%define		kpname		kde-gtk-config
Summary:	GTK2 and GTK3 Configurator for KDE
Name:		kp5-%{kpname}
Version:	5.15.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	fc76a4f8bdb2a031fdadff946514ae3d
Patch0:		x32.patch
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
%patch0 -p1

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gtk3_preview
%attr(755,root,root) %{_libexecdir}/gtk_preview
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kdegtkconfig.so
%attr(755,root,root) %{_libexecdir}/reload_gtk_apps
/etc/xdg/cgcgtk3.knsrc
#/etc/xdg/cgcicon.knsrc
/etc/xdg/cgctheme.knsrc
%{_iconsdir}/hicolor/*/apps/kde-gtk-config.png
%{_iconsdir}/hicolor/scalable/apps/kde-gtk-config.svgz
%dir %{_datadir}/kcm-gtk-module
%{_datadir}/kcm-gtk-module/preview.ui
%{_datadir}/kservices5/kde-gtk-config.desktop

