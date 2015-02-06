%define major 4
%define libname %mklibname ksflphone %{major}
%define libqt %mklibname qtsflphone %{major}
%define devname %mklibname ksflphone -d

Summary:	SFLPhone KDE client
Name:		sflphone-kde
Version:	1.3.0
Release:	2
License:	GPLv3+
Group:		Communications
Url:		http://sflphone.org/
Source0:	http://download.kde.org/stable/sflphone/%{version}/src/sflphone-client-kde-%{version}.tar.xz
Patch0:		sflphone-client-kde-1.3.0-plasma.patch
Patch1:		sflphone-client-kde-1.3.0-soname.patch
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	kdepimlibs4-devel

%description
This package contains the KDE client for SFLPhone.

%files -f %{name}.lang
%doc AUTHORS
%{_bindir}/sflphone-client-kde
%{_kde_applicationsdir}/sflphone-client-kde.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.plasma.applet.sflphone
%{_kde_appsdir}/sflphone-client-kde
%{_kde_datadir}/config.kcfg/sflphone-client-kde.kcfg
%{_kde_iconsdir}/hicolor/*/apps/sflphone-client-kde.*
%{_kde_services}/plasma-*-sflphone.desktop
%{_mandir}/man1/sflphone-client-kde.1*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for SFLPhone KDE client
Group:		System/Libraries

%description -n %{libname}
This package contains shared libraries for SFLPhone KDE client.

%files -n %{libname}
%{_kde_libdir}/libksflphone.so.%{major}
%{_kde_libdir}/libksflphone.so.%{version}

#----------------------------------------------------------------------------

%package -n %{libqt}
Summary:	Shared libraries for SFLPhone KDE client
Group:		System/Libraries
Conflicts:	%{_lib}ksflphone4 < 1.3.0

%description -n %{libqt}
This package contains shared libraries for SFLPhone KDE client.

%files -n %{libqt}
%{_kde_libdir}/libqtsflphone.so.%{major}
%{_kde_libdir}/libqtsflphone.so.%{version}

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libqt} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains development files for SFLPhone KDE client.

%files -n %{devname}
%doc AUTHORS DEVELOPPER
%{_kde_libdir}/libksflphone.so
%{_kde_libdir}/libqtsflphone.so
%{_includedir}/ksflphone/
%{_includedir}/qtsflphone/

#----------------------------------------------------------------------------

%prep
%setup -qn sflphone-client-kde-%{version}
%patch0 -p1
%patch1 -p1

%build
%global optflags %{optflags} -fno-strict-aliasing
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang sflphone-client-kde %{name} %{name}.lang --with-html

