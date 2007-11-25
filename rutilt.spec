#
# TODO:
# - desktop
# - figure out what's wrong with the helper (sudo rutilt suggested for now)
#
Summary:	Wireless devices configuration tool, with extra support for Ralink chipsets
Summary(pl.UTF-8):	Narzędzie do konfiguracji urządzeń bezprzewodowych z dodatkową obsługą układów Ralink
Name:		rutilt
Version:	0.15
Release:	0.1
License:	GPL v2
Group:		Applications
#Source0:	http://cbbk.free.fr/bonrom/?download=RutilTv%{version}.tar.gz
Source0:	RutilTv%{version}.tar.gz
# Source0-md5:	2a3858a24d0a1affa4b12c87e7015716
Patch0:		%{name}-FHS.patch
URL:		http://cbbk.free.fr/bonrom/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	linux-libc-headers
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RutilT - wireless devices configuration tool, with extra support for
Ralink chipsets.

%description -l pl.UTF-8
RutilT - narzędzie do konfiguracji urządzeń bezprzewodowych z
dodatkową obsługą układów Ralink.

%prep
%setup -q -n RutilTv%{version}
%patch0 -p1

%build
./configure.sh \
	--kernel_sources=%{_prefix} \
	--launcher=disabled \
	--prefix=%{_prefix}
%{__make} \
	OPTIONS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/rutilt

%{__make} install \
	RUTILT_PREFIX=$RPM_BUILD_ROOT%{_bindir} \
	HELPER_PREFIX=$RPM_BUILD_ROOT%{_libdir}/rutilt \
	IP_SCRIPT_PREFIX=$RPM_BUILD_ROOT%{_datadir}/rutilt \
	ICON_PREFIX=$RPM_BUILD_ROOT%{_pixmapsdir}/rutilt \
	DESKTOP_LAUNCHER_PREFIX=$RPM_BUILD_ROOT%{_datadir}/applications \
	RUTILT_MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir}/man1 \
	HELPER_MODE=755

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README INSTALL
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/rutilt.desktop
%{_mandir}/man1/rutilt.1*
%dir %{_pixmapsdir}/%{name}
%{_pixmapsdir}/%{name}/*.png
