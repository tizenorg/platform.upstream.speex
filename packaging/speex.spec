#
# spec file for package speex
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           speex
%define package_version 1.2rc1
Version:        1.1.999_%{package_version}
Release:        8
License:        BSD-3-Clause
Summary:        An Open Source, Patent Free Speech Codec
Url:            http://www.speex.org/
Group:          System/Libraries
Source:         %{name}-%{package_version}.tar.bz2
Source2:        baselibs.conf
Patch1:         speex-1.0.5-warning-fix.diff
Patch2:         speex-no-build-date.patch
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      speex-64bit
%endif

%description
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n libspeex1
License:        BSD-3-Clause
Summary:        An Open Source, Patent Free Speech Codec Library
Group:          System/Libraries
Obsoletes:      libspeex < %{version}
Provides:       libspeex = %{version}

%description -n libspeex1
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n libspeexdsp1
License:        BSD-3-Clause
Summary:        An Open Source, Patent Free Speech Codec Library
Group:          System/Libraries

%description -n libspeexdsp1
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
License:        BSD-3-Clause
Summary:        Development package for SpeeX
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libogg-devel
Requires:       libspeex1 = %{version}
Requires:       libspeexdsp1 = %{version}
Provides:       libspeex-devel = %{version}-%{release}
Obsoletes:      libspeex-devel < %{version}-%{release}
# bug437293
%ifarch ppc64
Obsoletes:      speex-devel-64bit
%endif
#

%description devel
This package contains the files needed to compile programs that use the
SpeeX library.

%prep
%setup -q -n %{name}-%{package_version}
%patch1
%patch2

%build
%if 0%{?suse_version} >= 1100
autoreconf -fi
%endif
%configure \
    --disable-static \
    --with-ogg-libraries=%{_libdir}
make %{?_smp_mflags}

%install
%make_install
# remove duped documents
rm -rf %{buildroot}%{_datadir}/doc/speex*
# remove unneeded *.la files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

%post -n libspeex1 -p /sbin/ldconfig

%postun -n libspeex1 -p /sbin/ldconfig

%post -n libspeexdsp1 -p /sbin/ldconfig

%postun -n libspeexdsp1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc doc/*.pdf
%{_bindir}/speex*
%{_mandir}/man?/*

%files -n libspeex1
%defattr(-,root,root)
%{_libdir}/libspeex.so.*

%files -n libspeexdsp1
%defattr(-,root,root)
%{_libdir}/libspeexdsp.so.*

%files devel
%defattr(-,root,root)
%doc doc/manual.pdf
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
