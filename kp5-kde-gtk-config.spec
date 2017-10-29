%define		kdeplasmaver	5.11.2
%define		qtver		5.3.2
%define		kpname		kde-gtk-config
Summary:	GTK2 and GTK3 Configurator for KDE
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	39bc7e719a90885162d473440540880e
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk3_preview
%attr(755,root,root) %{_libdir}/gtk_preview
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kdegtkconfig.so
%attr(755,root,root) %{_libdir}/reload_gtk_apps
/etc/xdg/cgcgtk3.knsrc
#/etc/xdg/cgcicon.knsrc
/etc/xdg/cgctheme.knsrc
%{_iconsdir}/hicolor/*/apps/kde-gtk-config.png
%{_iconsdir}/hicolor/scalable/apps/kde-gtk-config.svgz
%dir %{_datadir}/kcm-gtk-module
%{_datadir}/kcm-gtk-module/preview.ui
%{_datadir}/kservices5/kde-gtk-config.desktop

