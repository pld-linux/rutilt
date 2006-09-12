#
# TODO:
# - desktop
# - figure out what's wrong with the helper (sudo rutilt suggested for now)
#
Summary:	Wireless devices configuration tool, with extra support for Ralink chipsets
Summary(pl):	Narzêdzie do konfiguracji urz±dzeñ bezprzewodowych z dodatkow± obs³ug± uk³adów Ralink
Name:		rutilt
Version:	0.12
Release:	0.1
License:	GPL v2
Group:		Applications
#Source0:	http://cbbk.free.fr/bonrom/?download=RutilTv%{version}.tar.gz
Source0:	RutilTv%{version}.tar.gz
# Source0-md5:	c85810225e4369c7a27681ba0ed15903
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

%description -l pl
RutilT - narzêdzie do konfiguracji urz±dzeñ bezprzewodowych z
dodatkow± obs³ug± uk³adów Ralink.

%prep
%setup -q -n RutilTv%{version}
%patch0 -p1

%build
./configure.sh \
	--kernel_sources=/usr \
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
	ICON_PREFIX=$RPM_BUILD_ROOT%{_datadir}/rutilt \
	HELPER_MODE=755

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README INSTALL
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
