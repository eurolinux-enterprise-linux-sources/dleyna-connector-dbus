%global api 1.0
%global __provides_exclude_from ^%{_libdir}/dleyna-%{api}/connectors/.*\\.so$

Name:           dleyna-connector-dbus
Version:        0.2.0
Release:        1%{?dist}
Summary:        D-Bus connector for dLeyna services

License:        LGPLv2
URL:            https://01.org/dleyna/
Source0:        https://01.org/dleyna/sites/default/files/downloads/%{name}-%{version}.tar.gz
Patch0:         0001-Connector-Don-t-crash-when-trying-to-unwatch-non-exi.patch

BuildRequires:  dbus-devel
BuildRequires:  dleyna-core-devel
BuildRequires:  glib2-devel >= 2.28
BuildRequires:  pkgconfig autoconf automake libtool

%description
D-Bus connector for dLeyna services.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
autoreconf -f -i
%configure \
  --disable-silent-rules \
  --disable-static

make %{?_smp_mflags}


%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -delete


%files
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc README
%dir %{_libdir}/dleyna-%{api}
%dir %{_libdir}/dleyna-%{api}/connectors
%{_libdir}/dleyna-%{api}/connectors/libdleyna-connector-dbus.so

%files devel
%{_libdir}/pkgconfig/%{name}-%{api}.pc


%changelog
* Mon Jun 01 2015 Debarshi Ray <rishi@fedoraproject.org> - 0.2.0-1
- Initial RHEL import
Resolves: #1221261
