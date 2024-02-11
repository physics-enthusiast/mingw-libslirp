%{?mingw_package_header}

Name:		mingw-libslirp
Version:	4.7.0
Release:	1%{?dist}
Summary:	MinGW library for general purpose TCP-IP emulation functionality
 
License:	MIT and BSD-3-Clause
URL:		https://gitlab.freedesktop.org/slirp/libslirp
Source0:	https://gitlab.freedesktop.org/slirp/libslirp/-/archive/v%{version}/libslirp-v%{version}.tar.bz2

BuildArch:	noarch

BuildRequires: gcc
BuildRequires: meson
 
BuildRequires: mingw32-filesystem >= 107
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gcc
BuildRequires: mingw32-glib2
 
BuildRequires: mingw64-filesystem >= 107
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gcc
BuildRequires: mingw64-glib2
 
%description
Libslirp is a user-mode networking library used by virtual machines,
containers or various tools.
 
This is the MinGW build of Libslirp
 
 
# Win32
%package -n mingw32-libslirp
Summary:	    MinGW library for general purpose TCP-IP emulation functionality
Requires:       pkgconfig
 
%description -n mingw32-libslirp
Libslirp is a user-mode networking library used by virtual machines,
containers or various tools.
 
This is the MinGW build of Libslirp
 
# Win64
%package -n mingw64-libslirp
Summary:        MinGW library for general purpose TCP-IP emulation functionality
Requires:       pkgconfig
 
%description -n mingw64-libslirp
Libslirp is a user-mode networking library used by virtual machines,
containers or various tools.
 
This is the MinGW build of Libslirp
 
 
%{?mingw_debug_package}
 
 
%prep
%autosetup -p1 -n libslirp-v%{version}

%build
%mingw_meson \
  -Dintrospection=disabled

%mingw_ninja

%install
export DESTDIR=%{buildroot}
%mingw_ninja install
 
%mingw_find_lang libslirp
 
# Win32
%files -n mingw32-libslirp -f mingw32-libslirp.lang
%license COPYING
%{mingw32_bindir}/libslirp-0.dll
%{mingw32_includedir}/libslirp-version.h
%{mingw32_includedir}/libslirp.h
%{mingw32_libdir}/libslirp.a
%{mingw32_libdir}/libslirp.dll.a
%{mingw32_libdir}/pkgconfig/slirp.pc
 
# Win64
%files -n mingw64-libslirp -f mingw64-libslirp.lang
%license COPYING
%{mingw64_bindir}/libslirp-0.dll
%{mingw64_includedir}/libslirp-version.h
%{mingw64_includedir}/libslirp.h
%{mingw64_libdir}/libslirp.a
%{mingw64_libdir}/libslirp.dll.a
%{mingw64_libdir}/pkgconfig/slirp.pc
 
%changelog
* Sun Feb 11 2024 Placeholder <placeholder@email.org> - 2.25.5-1
- Initial release 
