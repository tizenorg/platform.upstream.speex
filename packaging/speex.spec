Name:           speex
%define package_version 1.2rc1
Version:        1.1.999_%{package_version}
Release:        9
License:        BSD-3-Clause
Summary:        An Open Source, Patent Free Speech Codec
Url:            http://www.speex.org/
Group:          Multimedia/Audio
Source:         %{name}-%{package_version}.tar.bz2
Source2:        baselibs.conf
Source1001: 	speex.manifest
BuildRequires:  libogg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n libspeex
License:        BSD-3-Clause
Summary:        An Open Source, Patent Free Speech Codec Library
Group:          Multimedia/Audio

%description -n libspeex
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package -n libspeexdsp
License:        BSD-3-Clause
Summary:        An Open Source, Patent Free Speech Codec Library
Group:          Multimedia/Audio

%description -n libspeexdsp
Speex is a patent free audio codec designed especially for voice
(unlike Vorbis which targets general audio) signals and providing good
narrowband and wideband quality. This project aims to be complementary
to the Vorbis codec.

%package devel
License:        BSD-3-Clause
Summary:        Development package for SpeeX
Group:          Development/Libraries
Requires:       glibc-devel
Requires:       libogg-devel
Requires:       libspeex = %{version}
Requires:       libspeexdsp = %{version}

%description devel
This package contains the files needed to compile programs that use the
SpeeX library.

%prep
%setup -q -n %{name}-%{package_version}
cp %{SOURCE1001} .

%build
autoreconf -fi
%configure \
    --disable-static \
    --with-ogg-libraries=%{_libdir}
make %{?_smp_mflags}

%install
%make_install
# remove duped documents
rm -rf %{buildroot}%{_datadir}/doc/speex*

%post -n libspeex -p /sbin/ldconfig

%postun -n libspeex -p /sbin/ldconfig

%post -n libspeexdsp -p /sbin/ldconfig

%postun -n libspeexdsp -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license COPYING
%{_bindir}/speex*
%{_mandir}/man?/*

%files -n libspeex
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libspeex.so.*

%files -n libspeexdsp
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libspeexdsp.so.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
