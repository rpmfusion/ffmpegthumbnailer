Name:           ffmpegthumbnailer
Version:        2.0.2
Release:        1%{?dist}
Summary:        Lightweight video thumbnailer that can be used by file managers

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://code.google.com/p/ffmpegthumbnailer/
Source0:        http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ffmpeg-devel, libpng-devel, libjpeg-devel
BuildRequires:  chrpath


%description
This video thumbnailer can be used to create thumbnails for your video files.

%package devel
Summary:        Headers and libraries for building apps that use ffmpegthumbnailer
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This video thumbnailer can be used to create thumbnails for your video files,
development package.

%prep
%setup -q
chmod -x README INSTALL COPYING AUTHORS


%build
%configure --enable-png \
           --enable-jpeg \
           --disable-static


make %{?_smp_mflags}

 
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/ffmpegthumbnailer
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README COPYING AUTHORS
%{_bindir}/ffmpegthumbnailer
%{_libdir}/libffmpegthumbnailer.so.4*
%{_mandir}/man1/ffmpegthumbnailer.1.gz

%files devel
%defattr(-,root,root,-)
%{_libdir}/libffmpegthumbnailer.so
%{_libdir}/pkgconfig/lib%{name}.pc
%dir %{_includedir}/libffmpegthumbnailer
%{_includedir}/libffmpegthumbnailer/*.h

%changelog
* Sun May 16 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.2-1
- version bump

* Sat Apr 19 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.1-1
- version bump
- libspatch.patch merged upstream, issue 59

* Mon Apr 12 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.0-3
- drop _kde4_ macros
- moving chmod to %%prep
- moving %%{_includedir}/libffmpegthumbnailer to -devel
- track sonames closer
- license change to GPLv2+
- remove duplicate docs from -devel
- patching libs in pkgconfig%%{name}.pc, thanks to rdieter

* Sun Apr 11 2010 leigh scott <leigh123linux@googlemail.com> 2.0.0-2
- fix rpath
- enable jpeg and png support
- clean up spec file
- remove static libs as they aren't needed
- add docs

* Sat Apr 10 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.0-1
- initial build
- has to be built with "QA_RPATHS=$[0x0001|0x0010 ]" for now
