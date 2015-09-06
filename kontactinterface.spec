#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

%define rel 1

Summary:        Kontact Plugin Interface Library
Name:           kontactinterface
Version: 15.08.0
Release:        %mkrel %rel
License:        GPLv2+
Group:          System/Base
Source0:        http://fr2.rpmfind.net/linux/KDE/stable/plasma/%{name}-%{version}.tar.xz

URL:            https://www.kde.org/

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Gui)

BuildRequires:  kf5-macros
BuildRequires:  ki18n-devel >= 5.12.0
BuildRequires:  kcoreaddons-devel >= 5.12.0
BuildRequires:  kparts-devel >= 5.12.0
BuildRequires:  kwindowsystem-devel >= 5.12.0
BuildRequires:  kxmlgui-devel >= 5.12.0
BuildRequires:  kiconthemes-devel >= 5.12.0

BuildRequires:  boost-devel

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Kontact Plugin Interface Library

%files
%_kf5_datadir/kservicetypes5/kontactplugin.desktop

#--------------------------------------------------------------------

%define kf5kontactinterface_major 4
%define libkf5kontactinterface %mklibname kf5kontactinterface %{kf5kontactinterface_major}

%package -n %libkf5kontactinterface
Summary:      Kontact Plugin Interface Library
Group:        System/Libraries
Requires:     %name = %version-%release

%description -n %libkf5kontactinterface
Kontact Plugin Interface Library

%files -n %libkf5kontactinterface
%_kf5_libdir/libKF5KontactInterface.so.%{kf5kontactinterface_major}*
%_kf5_libdir/libKF5KontactInterface.so.5

#--------------------------------------------------------------------

%define kf5kontactinterface_devel %mklibname kf5kontactinterface -d

%package -n %kf5kontactinterface_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libkf5kontactinterface = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %kf5kontactinterface_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kf5kontactinterface_devel
%_kf5_includedir/KontactInterface
%_kf5_includedir/kontactinterface_version.h
%_kf5_libdir/libKF5KontactInterface.so
%_kf5_libdir/cmake/KF5KontactInterface
%_qt5_prefix/mkspecs/modules/qt_KontactInterface.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kf5
%make

%install
%makeinstall_std -C build

%find_lang --all %{name}5



%changelog
* Wed Aug 19 2015 neoclust <neoclust> 15.08.0-1.mga6
+ Revision: 865962
- New version 15.08.0

* Wed Aug 12 2015 neoclust <neoclust> 15.07.90-2.mga6
+ Revision: 863681
- Plasma Mass Rebuild - Rebuild for new Plasma

* Sun Aug 09 2015 neoclust <neoclust> 15.07.90-1.mga6
+ Revision: 861775
- New version 15.07.90

* Tue Jul 28 2015 neoclust <neoclust> 15.07.80-3.mga6
+ Revision: 858734
- Split files out of the library

* Tue Jul 28 2015 neoclust <neoclust> 15.07.80-2.mga6
+ Revision: 858448
- Fix lib name

* Tue Jul 28 2015 neoclust <neoclust> 15.07.80-1.mga6
+ Revision: 858398
- imported package kontactinterface

