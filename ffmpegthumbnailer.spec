%global commit  aa8a6f99c5b9bd5ecdc50fda2b5a48de1eaefbde
%global date 20231018
%global shortcommit0 %(c=%{commit}; echo ${c:0:7})

Name:           ffmpegthumbnailer
Version:        2.2.3
Release:        0.6%{?shortcommit0:.%{date}git%{shortcommit0}}%{?dist}
Summary:        Lightweight video thumbnailer that can be used by file managers

License:        GPLv2+
URL:            https://github.com/dirkvdb/%{name}
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch0:         add_audio_cover.patch

BuildRequires:  ffmpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++


%description
This video thumbnailer can be used to create thumbnails for your video files.

%package devel
Summary:        Headers and libraries for building apps that use ffmpegthumbnailer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This video thumbnailer can be used to create thumbnails for your video files,
development package.

%prep
%autosetup -p1 -n %{name}-%{commit}
chmod -x README INSTALL COPYING AUTHORS

%build
%cmake -DENABLE_GIO=ON -DENABLE_THUMBNAILER=ON -GNinja

%cmake_build

 
%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc README AUTHORS
%license COPYING
%{_bindir}/ffmpegthumbnailer
%{_libdir}/libffmpegthumbnailer.so.4*
%{_mandir}/man1/ffmpegthumbnailer.1.gz
# gnome thumbnailer registration
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/ffmpegthumbnailer.thumbnailer

%files devel
%{_libdir}/libffmpegthumbnailer.so
%{_libdir}/pkgconfig/libffmpegthumbnailer.pc
%{_includedir}/libffmpegthumbnailer/


%changelog
* Sat Nov 11 2023 Sérgio Basto <sergio@serjux.com> - 2.2.3-0.6.20221021gite0bf01d
- Update latest git commits with GCC-13 fix

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.3-0.5.20210902gitd92e191
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 2.2.3-0.4.20210902gitd92e191
- Rebuild for new ffmpeg

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.3-0.3.20210902gitd92e191
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.2.3-0.2.20210902gitd92e191
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Leigh Scott <leigh123linux@gmail.com> - 2.2.3-0.1.20210902gitd92e191
- Update to git snapshot

* Thu Nov 11 2021 Leigh Scott <leigh123linux@gmail.com> - 2.2.2-10
- Rebuilt for new ffmpeg snapshot

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 31 2020 Leigh Scott <leigh123linux@gmail.com> - 2.2.2-7
- Rebuilt for new ffmpeg snapshot

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Leigh Scott <leigh123linux@gmail.com> - 2.2.2-5
- Improve compatibility with new CMake macro

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.2-4
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-2
- Add audio covers to mime types

* Wed Jan 08 2020 Leigh Scott <leigh123linux@googlemail.com> - 2.2.2-1
- Update ffmpegthumbnailer to 2.2.2

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 2.2.0-9
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-7
- Rebuild for ffmpeg-3.4.5 on el7
- Use ldconfig_scriptlets
- Use CMake3

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.0-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-3
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Sérgio Basto <sergio@serjux.com> - 2.2.0-1
- Update ffmpegthumbnailer to 2.2.0

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.1.2-3
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Sérgio Basto <sergio@serjux.com> - 2.1.2-1
- Update ffmpegthumbnailer to 2.1.2
- Clean up spec, add license tag.
- Fix changelog dates.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.1.1-2
- Rebuilt for ffmpeg-3.1.1

* Sat Jun 25 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-1
- 2.1.1

* Thu Apr 09 2015 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.9-1
- 2.0.9

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 2.0.8-11
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-10
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 2.0.8-9
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 2.0.8-8
- Rebuilt for ffmpeg-2.2

* Wed Nov 27 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-7
- fix compile error

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-6
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-5
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-4
- Rebuilt for x264/FFmpeg

* Mon Mar 04 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-3
- Rebuilt for F-19 Features

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-2
- Rebuilt for FFmpeg 1.0

* Wed Aug 29 2012 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.8-1
- 2.0.8

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-4
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.7-1
- new version
- patches merged upstream

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 2.0.6-3
- Rebuilt for FFmpeg-0.8*

* Sun Feb 13 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.6-2
- patch NULL reference to make rawhide build

* Fri Feb 04 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.6-1
- version bump
- patch libdl link issue
- add BR: automake and autoconf

* Sun Dec 05 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.5-1
- version bump
- enable gio-support

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.0.4-2
- rebuilt

* Wed Aug 18 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.4-1
- version bump

* Sun May 16 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.2-1
- version bump

* Mon Apr 19 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.1-1
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
