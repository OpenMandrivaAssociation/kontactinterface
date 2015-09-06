#
# Please do not update/rebuild/touch this package before asking first to mikala and/or neoclust
# This package is part of the KDE Stack.
#
#define debug_package %{nil}

Summary:        Kontact Plugin Interface Library
Name:           kontactinterface
Version:	15.08.0
Release:        1
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

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5IconThemes)

BuildRequires:  boost-devel

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

%description
Kontact Plugin Interface Library

%files
%_datadir/kservicetypes5/kontactplugin.desktop

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
%_libdir/libKF5KontactInterface.so.%{kf5kontactinterface_major}*
%_libdir/libKF5KontactInterface.so.5

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
%_includedir/KF5/KontactInterface
%_includedir/KF5/kontactinterface_version.h
%_libdir/libKF5KontactInterface.so
%_libdir/cmake/KF5KontactInterface
%_libdir/qt5/mkspecs/modules/qt_KontactInterface.pri

#--------------------------------------------------------------------

%prep
%setup -q 
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
