# http://lists.x.org/archives/xorg-devel/2009-February/000220.html
Summary:	X.org input driver for Calcomp devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla urządzeń Calcomp
Name:		xorg-driver-input-calcomp
Version:	1.1.2
Release:	3.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-calcomp-%{version}.tar.bz2
# Source0-md5:	ebc9a64dc72ae3015c16011bbd2d3557
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Calcomp devices. This driver supports the
Calcomp binary format used by the Drawing Board II and III series.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla urządzeń Calcomp. Ten sterownik
obsługuje format binarny Calcomp używany przez urządzenia z serii
Drawing Board II i III.

%prep
%setup -q -n xf86-input-calcomp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/calcomp_drv.so
%{_mandir}/man4/calcomp.4*
