%define major	4
%define libname	%mklibname ksflphone %{major}
%define devname	%mklibname ksflphone -d

Name:		sflphone-kde
Version:	1.2.0
Release:	1
Summary:	SFLPhone KDE client
License:	GPLv3+
Group:		Communications
Source0:	http://download.kde.org/stable/sflphone/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	kdepim4-devel

%description
This package contains the KDE client for SFLPhone.

%package -n %{libname}
Summary:	Shared libraries for SFLPhone KDE client
Group:		System/Libraries

%description -n %{libname}
This package contains shared libraries for SFLPhone KDE client.

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		Development/C++

%description -n %{devname}
This package contains development files for SFLPhone KDE client.

%prep
%setup -qn %{name}

%build
%cmake_kde4
%make

%install
pushd build
%makeinstall_std
popd

%files
%doc AUTHORS README
%doc %{_kde_docdir}/HTML/en/sflphone-client-kde
%{_bindir}/sflphone-client-kde
%{_kde_libdir}/kde4/plasma_engine_sflphone.so
%{_kde_applicationsdir}/sflphone-client-kde.desktop
%{_kde_appsdir}/plasma/plasmoids/org.kde.plasma.applet.sflphone
%{_kde_appsdir}/plasma/services/sflphone.operations
%{_kde_appsdir}/sflphone-client-kde
%{_kde_datadir}/config.kcfg/sflphone-client-kde.kcfg
%{_kde_iconsdir}/hicolor/*/apps/sflphone-client-kde.*
%{_kde_services}/plasma-*-sflphone.desktop
%{_mandir}/man1/sflphone-client-kde.1*

%files -n %{libname}
%{_kde_libdir}/libksflphone.so.%{major}
%{_kde_libdir}/libksflphone.so.%{version}
%{_kde_libdir}/libqtsflphone.so.%{major}
%{_kde_libdir}/libqtsflphone.so.%{version}

%files -n %{devname}
%doc AUTHORS DEVELOPPER README
%{_kde_libdir}/libksflphone.so
%{_kde_libdir}/libqtsflphone.so
%{_includedir}/ksflphone/
%{_includedir}/qtsflphone/
