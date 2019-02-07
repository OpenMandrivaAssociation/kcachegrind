Summary:	Visualisation tool for profiling data generated by Cachegrind and Calltree
Name:		kcachegrind
Version:	 18.12.2
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires: 	cmake
BuildRequires: 	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5KIO)
Requires:	valgrind

%description
KCachegrind is a visualisation tool for the profiling data generated by
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files -f %{name}.lang
%{_bindir}/kcachegrind
%{_bindir}/dprof2calltree
%{_bindir}/hotshot2calltree
%{_bindir}/memprof2calltree
%{_bindir}/op2calltree
%{_bindir}/pprof2calltree
%{_datadir}/kcachegrind
%{_datadir}/kxmlgui5/kcachegrind
%{_datadir}/applications/org.kde.kcachegrind.desktop
%{_datadir}/metainfo/org.kde.kcachegrind.appdata.xml
%{_iconsdir}/*/*/*/kcachegrind*

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html --with-qt
