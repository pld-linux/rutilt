#
# TODO:
# - desktop
# - figure out what's wrong with the helper (sudo rutilt suggested for now)
#
Summary:	Wireless devices configuration tool, with extra support for Ralink chipsets
Summary(pl.UTF-8):	Narzędzie do konfiguracji urządzeń bezprzewodowych z dodatkową obsługą układów Ralink
Name:		rutilt
Version:	0.18
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://bonrom.cbbknet.com/files/RutilTv%{version}.tar.gz
# Source0-md5:	c745af9fbadd3a843b6f8273b6eb71bd
Patch0:		%{name}-FHS.patch
URL:		http://cbbk.free.fr/bonrom/
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	linux-libc-headers
BuildRequires:	pkgconfig
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
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
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/rutilt

%{__make} install \
	RUTILT_PREFIX=$RPM_BUILD_ROOT%{_bindir} \
	HELPER_PREFIX=$RPM_BUILD_ROOT%{_libdir}/rutilt \
	IP_SCRIPT_PREFIX=$RPM_BUILD_ROOT%{_datadir}/rutilt \
	DATA_PREFIX=$RPM_BUILD_ROOT%{_datadir}/rutilt \
	ICON_16X16_PREFIX=$RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps \
	ICON_32X32_PREFIX=$RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps \
	ICON_48X48_PREFIX=$RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps \
	ICON_64X64_PREFIX=$RPM_BUILD_ROOT%{_iconsdir}/hicolor/64x64/apps \
	ICON_128X128_PREFIX=$RPM_BUILD_ROOT%{_iconsdir}/hicolor/128x128/apps \
	DESKTOP_LAUNCHER_PREFIX=$RPM_BUILD_ROOT%{_desktopdir} \
	MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir}/man1 \
	HELPER_MODE=755

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_postun
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%doc AUTHORS README INSTALL art/COPYING
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/rutilt.desktop
%{_mandir}/man1/rutilt.1*
%{_mandir}/man1/rutilt_helper.1*
%{_iconsdir}/hicolor/*/*/*.png
