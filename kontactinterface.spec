#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary:        Kontact Plugin Interface Library
Name:           kontactinterface
Version:	25.08.0
Release:	%{?git:0.%{git}.}1
License:        GPLv2+
Group:          System/Base
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kontactinterface/-/archive/%{gitbranch}/kontactinterface-%{gitbranchd}.tar.bz2#/kontactinterface-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kontactinterface-%{version}.tar.xz
%endif

URL:            https://www.kde.org/

BuildRequires:	cmake(Qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF6)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6IconThemes)

BuildRequires:  boost-devel

BuildRequires:	pkgconfig(xkbcommon)

BuildRequires:	libxml2-utils
BuildRequires:	docbook-dtds
BuildRequires:	docbook-style-xsl

# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

# Renamed after 6.0 2025-05-09
%rename plasma6-kontactinterface

%description
Kontact Plugin Interface Library

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kontactinterface.categories
%{_datadir}/qlogging-categories6/kontactinterface.renamecategories

#--------------------------------------------------------------------

%define kf6kontactinterface_major 6
%define libkf6kontactinterface %mklibname KPim6KontactInterface

%package -n %libkf6kontactinterface
Summary:      Kontact Plugin Interface Library
Group:        System/Libraries
Requires:     %name = %version-%release

%description -n %libkf6kontactinterface
Kontact Plugin Interface Library

%files -n %libkf6kontactinterface
%_libdir/libKPim6KontactInterface.so*

#--------------------------------------------------------------------

%define kf6kontactinterface_devel %mklibname KPim6KontactInterface -d

%package -n %kf6kontactinterface_devel

Summary:        Devel stuff for %name
Group:          Development/KDE and Qt
Requires:       %libkf6kontactinterface = %version-%release
Provides:       %name-devel = %{version}-%{release}

%description -n %kf6kontactinterface_devel
This package contains header files needed if you wish to build applications
based on %name.

%files -n %kf6kontactinterface_devel
%_includedir/KPim6/KontactInterface
%_libdir/cmake/KPim6KontactInterface
