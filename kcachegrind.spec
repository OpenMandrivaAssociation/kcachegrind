Summary:	Visualisation tool for profiling data generated by Cachegrind and Calltree
Name:		kcachegrind
Version:	16.04.3
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires: 	cmake
Requires:	valgrind

%description
KCachegrind is a visualisation tool for the profiling data generated by
Cachegrind and Calltree (they profile data file format is upwards compatible).
Calltree extends Cachegrind, which is part of Valgrind.

%files
%{_kde_bindir}/kcachegrind
%{_kde_bindir}/dprof2calltree
%{_kde_bindir}/hotshot2calltree
%{_kde_bindir}/memprof2calltree
%{_kde_bindir}/op2calltree
%{_kde_bindir}/pprof2calltree
%{_kde_appsdir}/kcachegrind
%{_kde_applicationsdir}/kcachegrind.desktop
%{_kde_iconsdir}/*/*/*/kcachegrind*
%{_kde_docdir}/*/*/kcachegrind

#----------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde4

%build
%make -C build

%install
%makeinstall_std -C build


